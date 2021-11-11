FROM node:7.5

ENV GITBOOK_HOME /data

RUN apt-get update --quiet && \
    apt-get install -y calibre && \
    npm install -g gitbook-cli && \
    gitbook fetch latest && \
    mkdir ${GITBOOK_HOME};

WORKDIR ${GITBOOK_HOME}
VOLUME ${GITBOOK_HOME}

EXPOSE 4000

CMD ["gitbook", "serve"]
