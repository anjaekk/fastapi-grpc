import grpc

from concurrent.futures import ThreadPoolExecutor
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import server.utils as utils
from database.models import Comments
from api.grpc_interface import Comments
from protobufs.comments_pb2_grpc import add_CommentsServicer_to_server

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=utils.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class GRPCServer:
    def __init__(self):
        self.server = grpc.aio.server(
            ThreadPoolExecutor(max_workers=5)
        )

    def add_service(self, service):
        add_CommentsServicer_to_server(service, self.server)

    async def start(self, host, port):
        self.server.add_insecure_port(f"{host}:{port}")
        await self.server.start()

    async def stop(self):
        await self.server.stop(0)


grpc_server = GRPCServer()
grpc_server.add_service(Comments())


@app.get("/")
async def health_check():
    return {"Health": True}


@app.on_event("startup")
async def startup():
    await grpc_server.start("0.0.0.0", 50051)


@app.on_event("shutdown")
async def shutdown():
    await grpc_server.stop()