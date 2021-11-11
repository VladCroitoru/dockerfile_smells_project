FROM alpine:3.7

RUN apk add g++

COPY . /src

WORKDIR /src

RUN chmod +x /src/entrypoint.sh

ENTRYPOINT [ "/src/entrypoint.sh" ]