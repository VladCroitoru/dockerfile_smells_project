FROM quay.io/blueshoe/python3.9-slim as base

FROM base as builder

ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y gcc python3-dev libpq-dev g++ git
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --prefix=/install -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local
# additional requirements for prod things
RUN apt update && apt install -y postgresql-client

RUN mkdir /app
COPY src/ /app
WORKDIR /app
