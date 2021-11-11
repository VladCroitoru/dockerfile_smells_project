FROM alpine:latest

LABEL maintainer="Sandro Lutz <code@temparus.ch>"

RUN apk add --no-cache python3 git

ADD . /git-mirror/

WORKDIR /git-mirror

RUN pip3 install -r requirements.txt
RUN chmod 755 docker.sh git-mirror.py

ENTRYPOINT ["./docker.sh"]