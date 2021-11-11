FROM node:9-alpine
ENV NODE_TLS_REJECT_UNAUTHORIZED=0
RUN npm -g install artillery
VOLUME /work
WORKDIR /work
ENTRYPOINT [ "/usr/local/bin/artillery" ]
