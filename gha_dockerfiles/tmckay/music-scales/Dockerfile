FROM python:3.9-slim-buster

RUN apt-get update && apt-get -y install gcc libcairo2-dev pkg-config python3-dev

WORKDIR /app

COPY requirements.txt  ./ 
RUN pip3 install --requirement requirements.txt

COPY setup.py ./
COPY mypy.ini ./
COPY music_scales music_scales/
COPY web web/
RUN pip3 install .
