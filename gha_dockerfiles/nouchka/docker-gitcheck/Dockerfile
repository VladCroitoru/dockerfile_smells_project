FROM python:alpine
LABEL maintainer="Jean-Avit Promis docker@katagena.com"
LABEL org.label-schema.vcs-url="https://github.com/nouchka/docker-gitcheck"
LABEL version="latest"

# Install requirements installation
RUN apk add --update git && rm -rf /var/cache/apk/* && \
	pip install git+git://github.com/mataneli94/gitcheck.git@master

VOLUME /files
WORKDIR /files

ENTRYPOINT [ "gitcheck" ]
