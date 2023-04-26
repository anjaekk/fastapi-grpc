from grpc_tools import protoc
import logging

logging.basicConfig(level=logging.INFO)


protoc.main(
    (
        '',
        '-I.',
        '--python_out=./protobufs',
        '--pyi_out=./protobufs',
        '--grpc_python_out=./protobufs',
        'comments.proto'
    )
)