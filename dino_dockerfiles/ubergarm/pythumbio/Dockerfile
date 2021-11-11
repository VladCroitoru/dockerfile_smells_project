FROM ubergarm/sanic-alpine

RUN apk add --no-cache \
    ffmpeg \
    openssl \
    ca-certificates && \
    pip3 install aiohttp

COPY ./server.py /server.py

ENTRYPOINT ["/usr/bin/python3"]

CMD ["/server.py"]
