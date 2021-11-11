FROM linuxserver/transmission

LABEL maintainer "zaggash"

# install packages and NzbToMedia Requirements
RUN \
 apk del --no-cache \
 	transmission-cli \
	transmission-daemon && \
 apk add --no-cache \
 	git \
	python \
	transmission-cli \
	transmission-daemon && \


 git -C /app clone -q  https://github.com/clinton-hall/nzbToMedia.git && \

 rm -rf /var/cache/apk/* /tmp/*

# copy local files
COPY root/ /
