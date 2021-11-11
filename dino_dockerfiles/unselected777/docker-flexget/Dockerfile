FROM python:3.5-alpine
RUN pip install flexget
RUN addgroup -g 1000 -S flexget && \
    adduser -u 1000 -S flexget -G flexget

USER flexget
WORKDIR /home/flexget 

ENTRYPOINT flexget
