FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app /app/