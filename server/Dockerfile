FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

EXPOSE 50051

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev

WORKDIR /app
COPY . /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python grpc_codegen.py