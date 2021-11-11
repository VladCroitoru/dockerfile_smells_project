FROM ubuntu:latest

MAINTAINER Matthieu Destombes "matthieu.destombes@activus-services.fr"
LABEL version="1.0"
LABEL description="This image emits a regular message on STDIN"

COPY ./heartbeat.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENV HEARTBEATSTEP 2

ENTRYPOINT ["/entrypoint.sh"]

CMD ["Heartbeat"]
