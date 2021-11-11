FROM jfloff/alpine-python:3.6-slim

ARG OASV_REF=0.2.0

RUN pip install "openapi-spec-validator==${OASV_REF}"

ENTRYPOINT ["/usr/bin/python", "-m", "openapi_spec_validator"]
