FROM alpine:3.3
MAINTAINER Stanislav Ovsiannikov "naphaso@gmail.com"

ENV NGINX_VERSION 1.9.11
ENV NGINX_PUSH_STREAM_VERSION 0.5.1
ENV NGINX_LUA_VERSION 0.10.1rc0

COPY packages /packages
RUN apk add --allow-untrusted --update \
#	packages/build/x86_64/nginx-1.9.11-r0.apk \
	packages/build/x86_64/nginx-common-1.9.11-r0.apk \
#	packages/build/x86_64/nginx-doc-1.9.11-r0.apk \
#	packages/build/x86_64/nginx-lua-1.9.11-r0.apk \
	packages/build/x86_64/nginx-pushstream-1.9.11-r0.apk \
#	packages/build/x86_64/nginx-rtmp-1.9.11-r0.apk \
#	packages/build/x86_64/nginx-vim-1.9.11-r0.apk \
	&& rm -rf /packages /var/cache/apk/* \
	&& ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log \
	&& mkdir /run/nginx

EXPOSE 80 443

VOLUME ["/etc/nginx"]
WORKDIR /etc/nginx

CMD ["nginx", "-g", "daemon off;"]

