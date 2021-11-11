FROM ubuntu:14.04

RUN apt-get update && apt-get install -y stone

CMD stone $DEST_HOST:$DEST_PORT $LISTEN_PORT
