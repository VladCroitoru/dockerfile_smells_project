FROM alpine:latest
RUN apk update && apk add curl git openssh-client
RUN curl https://caddyserver.com/download/linux/amd64?plugins=http.expires,http.git,http.ipfilter,http.proxyprotocol,http.ratelimit,net,tls.dns.cloudflare > caddy.tar.gz && \
	tar -zxvf caddy.tar.gz caddy -C /bin && \
	rm caddy.tar.gz
ENTRYPOINT ["/bin/caddy"]
