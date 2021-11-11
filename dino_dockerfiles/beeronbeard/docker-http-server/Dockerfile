FROM node:slim

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/BeerOnBeard/docker-http-server.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="1.0.0-rc1"

RUN npm install -g http-server
WORKDIR /www
VOLUME /www
EXPOSE 80
CMD ["http-server", "-p 80"]
