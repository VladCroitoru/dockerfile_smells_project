# Note: The newer busybox:glibc is missing libpthread.so.0.
FROM ubuntu:trusty
MAINTAINER Werner Beroux <werner@beroux.com>

RUN apt-get update && apt-get install -y ngrok-client

COPY entrypoint.sh /usr/local/bin

EXPOSE 4040

CMD ["entrypoint.sh"]
