FROM alpine:edge

ENV RUNOPTS = ""
ENV FORMAT = ""
ENV URL = ""

VOLUME /output

RUN apk update \
	&& apk add py2-pip ca-certificates \
	&& apk add ffmpeg \
	&& apk add gosu --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted \
	&& rm -rf /var/cache/apk/*

RUN pip install youtube-dl

ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT /entrypoint.sh
