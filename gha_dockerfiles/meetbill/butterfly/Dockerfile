FROM python:2-alpine

COPY ./butterfly /opt/butterfly

EXPOSE 8585
ENTRYPOINT ["sh","/opt/butterfly/run.sh","docker_start"]
