FROM python:3.6-slim

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
      libpq-dev \
      gcc \
      make \
    && apt-get clean \
    && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

WORKDIR /opt/server

COPY requirements.txt /opt/server
COPY src /opt/server/src
COPY setup.py /opt/server/

RUN ["/bin/sh", "-c", "pip install -r requirements.txt && pip install -e ."]

EXPOSE 8000

CMD ["/bin/sh", "-c", "-v", "-x", "python -m sanic sample_stream.app.app --host=0.0.0.0"]
