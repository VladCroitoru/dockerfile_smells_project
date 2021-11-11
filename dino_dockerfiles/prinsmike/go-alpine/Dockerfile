FROM golang:alpine
MAINTAINER prinsmike

RUN apk add --update sudo bash curl git mercurial										&& \
		curl https://glide.sh/get | sh													&& \
		echo "ALL						ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers

