FROM thortz/docker-xenial

ADD app/ /app
WORKDIR /app

RUN apt-get update && apt-get install -y curl deluged deluge-web deluge-webui apt-utils

RUN chmod +x /app/startup.sh

# ports and volumes
EXPOSE 8112/tcp 6881-6891/udp 58846

ENTRYPOINT ["/app/startup.sh","startup"]

