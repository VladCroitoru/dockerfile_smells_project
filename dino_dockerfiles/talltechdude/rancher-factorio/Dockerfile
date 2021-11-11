FROM krallin/ubuntu-tini

ENV VERSION=0.14.22

RUN apt-get update && apt-get install -y curl tini && \
	curl -skSL https://www.factorio.com/get-download/$VERSION/headless/linux64 \
		-o /tmp/factorio_headless_x64_$VERSION.tar.gz && \
	tar xzf /tmp/factorio_headless_x64_$VERSION.tar.gz --directory /opt && \
	rm /tmp/factorio_headless_x64_$VERSION.tar.gz && \
	apt-get remove --purge -y curl && \
	apt-get autoremove -y && \
	chmod +x /opt/factorio/bin/x64/factorio

WORKDIR /opt/factorio

COPY files/map-gen-settings.json /opt/factorio/data
COPY files/server-settings.json /opt/factorio/data
COPY files/run.sh /opt/factorio

ENV FACTORIO_SAVE_NAME=factorio
ENV FACTORIO_PORT=

VOLUME /opt/factorio/saves
VOLUME /opt/factorio/mods
VOLUME /opt/factorio/data

EXPOSE 34197/udp

CMD ["/opt/factorio/run.sh"]
