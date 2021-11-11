FROM openresty/openresty:alpine-fat
# See: https://hub.docker.com/_/nginx/
# See: https://github.com/openresty/docker-openresty/blob/master/alpine/Dockerfile
# TODO: Only keep luarocks and build env arround during build

# Add OpenResty stuff to path
ENV PATH=/usr/local/openresty/luajit/bin:/usr/local/openresty/nginx/sbin:/usr/local/openresty/bin:$PATH

RUN \
	# Add gettext for envsubst
	apk add --no-cache gettext &&\
	# Keep configuration files in /etc/nginx
	ln -sf /usr/local/openresty/nginx/conf /etc/nginx &&\
	# Install lua-resty-auto-ssl
	# See: https://github.com/GUI/lua-resty-auto-ssl
	apk add --no-cache curl bash openssl bash curl grep sed &&\
	luarocks install lua-resty-auto-ssl &&\
	mkdir /etc/resty-auto-ssl &&\
	chown nobody /etc/resty-auto-ssl

# Add proxy config
COPY init.sh /init.sh
COPY *.conf /etc/nginx/

# Add Let's Encrypt root certificate for OCSP stapling
COPY isrgrootx1.pem /etc/ssl/

EXPOSE 80
EXPOSE 443
HEALTHCHECK --interval=5m --timeout=3s \
	CMD curl -k -f https://localhost/ || exit 1

ENTRYPOINT ["/init.sh"]
