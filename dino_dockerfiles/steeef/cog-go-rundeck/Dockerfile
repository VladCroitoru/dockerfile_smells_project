FROM alpine:3.5
MAINTAINER Stephen Price <stephen@stp5.net>

COPY scripts/* /bundle/
WORKDIR /bundle
RUN chmod +x ./*.sh
COPY ./cog-go-rundeck /bundle/cog-go-rundeck
