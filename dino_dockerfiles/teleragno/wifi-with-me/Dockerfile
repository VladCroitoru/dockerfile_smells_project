FROM debian

RUN apt-get update && \
    apt-get install -y python-bottle

ENV BIND_ADDR="0.0.0.0"

COPY . /app/
WORKDIR /app
RUN python backend.py createdb \
    python backend.py buildgeojson

ENTRYPOINT ["python", "backend.py"]
