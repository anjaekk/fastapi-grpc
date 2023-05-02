from grpc_tools import protoc

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