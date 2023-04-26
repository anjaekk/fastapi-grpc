import grpc
from protobufs.comments_pb2 import (
    CreateCommentsRequest, 
    CreateCommentsResponse
)
from protobufs.comments_pb2_grpc import CommentsServicer
from .services import get_comment


class Comments(CommentsServicer):
    async def Create(
        self, request: CreateCommentsRequest, context: grpc.aio.ServicerContext
    ) -> CreateCommentsResponse:
        await get_comment()
        return CreateCommentsResponse(success=True)
