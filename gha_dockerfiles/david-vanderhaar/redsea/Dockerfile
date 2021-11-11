FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app

ARG SPLEETER_VERSION=1.5.3

ENV MODEL_PATH /model

RUN mkdir -p /model
RUN apt-get update && apt-get install -y ffmpeg libsndfile1
RUN pip install musdb museval
RUN pip install spleeter==${SPLEETER_VERSION}
RUN pip install python-multipart
RUN pip install aiofiles
RUN pip install numpy==1.19
