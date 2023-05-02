import os
import asyncio
import grpc
import logging
from fastapi import FastAPI
from django.core.handlers.wsgi import WSGIRequest

from .protobufs.comments_pb2_grpc import CommentsStub
from .protobufs.comments_pb2 import CreateCommentsRequest


app = FastAPI()

logger = logging.getLogger(__name__)

server_host = os.environ.get("GRPC_SERVER_HOST")
server_port = os.environ.get("GRPC_SERVER_PORT")
server_tls_url = os.environ.get("GRPC_SERVER_URL")
sercer_url = f"{server_host}:{server_port}"

# only prod server uses tls
is_server_tls = os.environ.get("SERVER_STATUS") == "prod"

async def comment_create_grpc_request(
        user: int, 
        status: str, 
        content: str
    ):
    if is_server_tls:
        creds = grpc.ssl_channel_credentials()
        options=(('grpc.ssl_target_name_override', server_tls_url),)
        grpc_channel = grpc.secure_channel(
            sercer_url, creds, options=options
        )
    else:
        grpc_channel = grpc.aio.insecure_channel(sercer_url)
    with grpc_channel as channel:
        stub = CommentsStub(channel)
        response = stub.Create(
            CreateCommentsRequest(
                user=user,
                status=status,
                content=content
            )
        )
        if not response.success:
            logger.error(
                f"Grpc create error"
            )

@app.get("/")
async def health_check():
    return {"Health": True}

if __name__ == "__main__":
    asyncio.run(
        comment_create_grpc_request(
            1,
            "pending",
            "comment example"
        )
    )
    
    
    
    
    
    
    
    
    
    
    