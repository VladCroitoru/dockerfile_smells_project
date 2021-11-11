FROM java:8

ENV VERSION 3.1.0

RUN mkdir -p /opt/imply
WORKDIR /opt/imply
RUN curl -O https://static.imply.io/release/imply-${VERSION}.tar.gz && \
	tar -xzf imply-${VERSION}.tar.gz && \
	ln -sf imply-${VERSION} current && \
	rm imply-${VERSION}.tar.gz && \
	rm -rf current/dist/druid/ && \
	rm -rf current/dist/zk && \
	rm -rf current/dist/tranquility

WORKDIR /opt/imply/current

EXPOSE 9095
CMD ["bin/supervise", "-c", "conf/supervise/quickstart.conf"]
