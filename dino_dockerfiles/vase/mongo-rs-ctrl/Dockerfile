FROM alpine:edge

RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories \
	&& apk add --no-cache mongodb docker \
	&& rm /usr/bin/mongos /usr/bin/mongoperf /usr/bin/mongosniff /usr/bin/mongod \
	&& rm /usr/bin/dockerd /usr/bin/docker-containerd /usr/bin/docker-containerd-ctr \
	&& rm /usr/bin/docker-containerd-shim /usr/bin/docker-proxy /usr/bin/docker-runc

COPY ctrl.sh /root
CMD /root/ctrl.sh
