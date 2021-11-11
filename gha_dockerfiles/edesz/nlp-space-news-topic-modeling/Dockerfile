# FROM python:3.8.6-slim-buster
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

ARG AZURE_STORAGE_KEY_ARG=abcd
ARG ENDPOINT_SUFFIX_ARG=abcd
ARG AZURE_STORAGE_ACCOUNT_ARG=abcd
ARG PORT_ARG=3080
ARG PY_VERSION=3.8

WORKDIR /api

COPY ./api /api
# RUN ls -la /api/*

RUN python -m pip install --upgrade pip \
    && pip install -r requirements.txt \
    && find /usr/local/lib/python$PY_VERSION -name '*.c' -delete \
    && find /usr/local/lib/python$PY_VERSION -name '*.pxd' -delete \
    && find /usr/local/lib/python$PY_VERSION -name '*.pyd' -delete \
    && find /usr/local/lib/python$PY_VERSION -name '__pycache__' | xargs rm -r
# RUN pip freeze

ENV AZURE_STORAGE_KEY=$AZURE_STORAGE_KEY_ARG \
    ENDPOINT_SUFFIX=$ENDPOINT_SUFFIX_ARG \
    AZURE_STORAGE_ACCOUNT=$AZURE_STORAGE_ACCOUNT_ARG \
    PORT=$PORT_ARG

# EXPOSE $PORT

# ENTRYPOINT [ "python3" ]
# CMD ["main.py"]
