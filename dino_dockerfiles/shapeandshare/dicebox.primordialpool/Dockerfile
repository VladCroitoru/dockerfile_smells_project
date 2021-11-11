# FROM tensorflow/tensorflow:latest-gpu
# FROM tensorflow/tensorflow
FROM python:3.7

WORKDIR .

COPY ./src/app /app
COPY requirements.txt /app
COPY dicebox.config /app
COPY dicebox.lonestar.json /app

RUN pip install -r /app/requirements.txt \
    && useradd -M -U -u 1000 primordialpool \
    && chown -R primordialpool /app

ENTRYPOINT ["python", "./primordialpool.py"]

