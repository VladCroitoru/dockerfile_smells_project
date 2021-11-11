ARG PYTHON3_VERSION=3.6

FROM python:${PYTHON3_VERSION}

RUN apt-get update && \
    apt-get install -y graphviz

WORKDIR /opt/seek-well

COPY scripts/ scripts/
COPY README.md .
COPY setup.py .

RUN python3 -m pip install -e .

ENTRYPOINT ["seek-well"]
