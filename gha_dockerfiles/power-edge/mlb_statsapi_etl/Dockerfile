# https://gallery.ecr.aws/bitnami/java
# - NO PYTHON public.ecr.aws/bitnami/java:1.8
# - NO JAVA public.ecr.aws/bitnami/python:3.9.5
#FROM public.ecr.aws/bitnami/java:1.8.292 AS BITNAMI_JAVA
FROM public.ecr.aws/bitnami/python:3.9.5 as main

# RUN apt-get update && apt-get install -y jq

ARG PYTHON_BASE_IMAGE="public.ecr.aws/bitnami/python:3.9.5"
ARG MLB_STATSAPI_REPO=power-edge/mlb_statsapi_etl
ARG MLB_STATSAPI_BRANCH=master
ARG MLB_STATSAPI_VERSION=latest
ARG MLB_STATSAPI_PIP_VERSION=21.1

ENV MLB_STATSAPI_VERSION=${MLB_STATSAPI_VERSION} \
    MLB_STATSAPI_PIP_VERSION=${MLB_STATSAPI_PIP_VERSION} \
    PYTHON_BASE_IMAGE=${PYTHON_BASE_IMAGE} \
    DEBIAN_FRONTEND=noninteractive LANGUAGE=C.UTF-8 LANG=C.UTF-8 LC_ALL=C.UTF-8 LC_CTYPE=C.UTF-8 LC_MESSAGES=C.UTF-8


COPY ./configs /app/mlb_statsapi_etl/configs
COPY ./docker /app/mlb_statsapi_etl/docker

RUN python -m pip install -r "/app/mlb_statsapi_etl/docker/requirements.txt"

COPY src /app/mlb_statsapi_etl/src
COPY setup.py /app/mlb_statsapi_etl/setup.py

RUN python -m pip install -e /app/mlb_statsapi_etl

ENTRYPOINT ["mlb_statsapi_etl/docker/entrypoint.sh"]

CMD ["python", "-u", "mlb_statsapi_etl/src/mlb_statsapi/cli.py"]
