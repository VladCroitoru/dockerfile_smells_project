FROM python:2.7-alpine


ADD ./listen_docker_hooks.py /listen_docker_hooks.py
ADD ./run.sh /run.sh

RUN apk add --no-cache --update docker curl && \
    pip install requests && \
    rm -f /usr/bin/docker* && \
    chmod +x /run.sh

## Ugly trick to get Docker client 1.12 in Alpine ...
ADD ./docker/ /usr/bin/

VOLUME /var/run/docker.sock

EXPOSE 8555
CMD ["/run.sh"]
