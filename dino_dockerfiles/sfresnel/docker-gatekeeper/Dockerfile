FROM sfresnel/docker-nodejs:1.0

RUN git clone https://github.com/prose/gatekeeper.git && \
	cd gatekeeper && \
	npm install

EXPOSE 9999

WORKDIR /gatekeeper
ENTRYPOINT ["node", "server.js"]