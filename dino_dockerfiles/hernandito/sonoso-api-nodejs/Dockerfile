FROM lsiobase/alpine:3.5

WORKDIR /src

# set version label
ARG BUILD_DATE
ARG VERSION
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:- ${BUILD_DATE}"

RUN apk update

#RUN \
# apk add --no-cache --virtual=build-dependencies \
#	curl \
#	mc \
#	tar && \

# apk add --no-cache \
#	nodejs \
#	openssl \
#	python && \

# copy local files
COPY root/ /

# ports and volumes
EXPOSE 5008
VOLUME /src
ENV TERM=xterm
