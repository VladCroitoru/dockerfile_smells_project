FROM alpine:3.12.0
ENV PATH /usr/games:$PATH

RUN apk update && \
    apk add --no-cache sl

RUN adduser --disabled-password conductor
USER conductor
ENTRYPOINT [ "sl" ]
