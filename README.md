# fastapi-grpc
⚡️Implementing fastapi asynchronous service with grpc based on docker container.⚡️

### Project Structure
```
├── Dockerfile
├── api
│   ├── __init__.py
│   ├── grpc_interface.py
│   └── services.py
├── comments.proto
├── database
│   ├── __init__.py
│   ├── config.py
│   ├── enums.py
│   └── models.py
├── grpc_codegen.py
├── main.py
├── protobufs
│   ├── __init__.py
│   ├── comments_pb2.py
│   ├── comments_pb2.pyi
│   └── comments_pb2_grpc.py
├── requirements.txt
└── utils.py
```
