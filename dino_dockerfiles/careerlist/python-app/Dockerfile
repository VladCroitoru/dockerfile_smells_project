ARG PYTHON_TAG=3.7.7-slim
FROM python:${PYTHON_TAG}

ARG PYTHON_TAG
ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.python-tag=${PYTHON_TAG} \
      org.label-schema.build-date=${BUILD_DATE} \
      org.label-schema.vcf-ref=${VCS_REF} \
      org.label-schema.URL="https://github.com/careerlist/python-app" \
      maintainer="https://github.com/careerlist"

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    build-essential \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir virtualenv \
  && rm -rf /root/.cache/pip/* \
  && virtualenv env

ENV WORKDIR /app

RUN mkdir -p ${WORKDIR}

WORKDIR ${WORKDIR}
