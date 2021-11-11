FROM alpine as buildstage

ENV GITASOF 21.06.27.1

ENV WORKDIR /kiwiirc
WORKDIR ${WORKDIR}

RUN apk add --update git yarn nodejs-npm g++ make go pkgconfig bash curl
RUN git clone --depth=1 --single-branch https://github.com/kiwiirc/kiwiirc
RUN cd /kiwiirc/kiwiirc && yarn install
RUN cd /kiwiirc/kiwiirc && npm run build

RUN cd /kiwiirc && git clone --depth=1 --single-branch https://github.com/kiwiirc/webircgateway
RUN cd /kiwiirc/webircgateway && \
        go get github.com/kiwiirc/webircgateway && \
        go build -o webircgateway main.go

FROM alpine as runstage

RUN apk add --no-cache su-exec

ENV WORKDIR /kiwiirc
WORKDIR ${WORKDIR}

COPY --from=buildstage ${WORKDIR}/kiwiirc/dist ${WORKDIR}/www
COPY --from=buildstage ${WORKDIR}/webircgateway/webircgateway ${WORKDIR}/kiwiirc
COPY --from=buildstage ${WORKDIR}/webircgateway/config.conf.example ${WORKDIR}/

RUN sed -i 's/^port = 80\b/port = 8080/' ${WORKDIR}/config.conf.example

EXPOSE 8080

VOLUME /kiwiirc-data

COPY docker-entrypoint.sh ${WORKDIR}/docker-entrypoint.sh

ENTRYPOINT ["/kiwiirc/docker-entrypoint.sh"]
CMD ["su-exec", "guest", "/kiwiirc/kiwiirc"]
