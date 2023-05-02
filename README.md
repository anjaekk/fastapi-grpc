# python-fastapi-tls-grpc
⚡️Implementing fastapi asynchronous service with tls grpc based on docker container.⚡️

(The project in progress...)

### Project Structure
```
.
├── README.md
├── docker-compose.yaml
├── envoy.yaml
├── python-client
│   ├── Dockerfile
│   ├── comments.proto
│   ├── grpc_codegen.py
│   ├── mian.py
│   ├── protobufs
│   │   ├── __init__.py
│   │   ├── comments_pb2.py
│   │   ├── comments_pb2.pyi
│   │   └── comments_pb2_grpc.py
│   └── requirements.txt
├── server
│   ├── Dockerfile
│   ├── api
│   │   ├── __init__.py
│   │   ├── grpc_interface.py
│   │   └── services.py
│   ├── comments.proto
│   ├── database
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── enums.py
│   │   └── models.py
│   ├── grpc_codegen.py
│   ├── main.py
│   ├── protobufs
│   │   ├── __init__.py
│   │   ├── comments_pb2.py
│   │   ├── comments_pb2.pyi
│   │   └── comments_pb2_grpc.py
│   ├── requirements.txt
│   └── utils.py
└── www.example.com
    ├── fullchain.pem
    └── privkey.pem
```
