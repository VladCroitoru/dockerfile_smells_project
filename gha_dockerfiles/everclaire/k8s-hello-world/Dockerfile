FROM ubuntu:20.04

ENV HELLOWORLD_RELEASE_VERSION="0.1a"
ENV API_PORT="8080"
ENV API_HOST="127.0.0.1"

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y update \
    && apt-get -y dist-upgrade \
    && apt-get -y install python3 python3-pip \
    && pip3 install fastapi uvicorn \
    && mkdir -p /app/python/

COPY helloworld.py /app/python/

COPY entrypoint.sh /app/python/

#COPY .env_vars /app/python/

RUN chmod 755 /app/python/entrypoint.sh

WORKDIR /app/python/

# CMD [ "uvicorn", "helloworld:api", "--host", "0.0.0.0", "--port", "8080"]
ENTRYPOINT ["/app/python/entrypoint.sh"]
