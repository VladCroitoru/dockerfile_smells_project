FROM python:3.8.5-slim
MAINTAINER Ji.Zhilong <zhilongji@gmail.com>

ENV PIP_INDEX_URL https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -U pip poetry && poetry config virtualenvs.create false
ADD . /app
WORKDIR /app
RUN poetry install
