#https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
FROM python:3.9

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p MachineLearning/models

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "6532", "--root-path", "/ml"]
