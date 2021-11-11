FROM harbor.computational.bio.uni-giessen.de/bakta/datastager:0.4.1 as stager

FROM docker.io/curlimages/curl:latest as linkerd
ARG LINKERD_AWAIT_VERSION=v0.2.3
RUN curl -sSLo /tmp/linkerd-await https://github.com/linkerd/linkerd-await/releases/download/release%2F${LINKERD_AWAIT_VERSION}/linkerd-await-${LINKERD_AWAIT_VERSION}-amd64 && \
    chmod 755 /tmp/linkerd-await


FROM oschwengers/bakta:v1.2.2
COPY --from=linkerd /tmp/linkerd-await /bin/linkerd-await

COPY --from=stager /DataStager /bin
COPY run.sh /bin

RUN chmod 555 /bin/run.sh

ENTRYPOINT ["/bin/linkerd-await", "--shutdown", "--"]
CMD  ["/bin/run.sh"]
