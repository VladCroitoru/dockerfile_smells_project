FROM anapsix/alpine-java:8

WORKDIR /bungee

ARG VERSION=1288

RUN apk --update add ca-certificates wget && \
	update-ca-certificates && \
	rm -rf /var/cache/apk/* && \
	wget -nv https://ci.md-5.net/job/BungeeCord/${VERSION}/artifact/bootstrap/target/BungeeCord.jar && \
	wget -nv https://github.com/syuchan1005/bungeecord-proxy/releases/download/1.0/bungeecord-proxy-dependencies.jar

COPY start.sh /bungee

RUN chmod +x start.sh

EXPOSE 25577
ENTRYPOINT ["./start.sh"]