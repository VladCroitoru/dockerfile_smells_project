FROM registry.fedoraproject.org/fedora-minimal
LABEL maintainer "spider@modio.se"

ENV LANG  C.utf8
ENV LANGUAGE C.utf8
ENV LC_ALL C.utf8

RUN microdnf install python3-pip openssl && \
    microdnf clean all                   && \
    pip3 install caramel-client          && \
    rm -rf ~/.cache/pip

VOLUME ["/data"]
WORKDIR /data
ENTRYPOINT ["caramel-client"]
CMD []
