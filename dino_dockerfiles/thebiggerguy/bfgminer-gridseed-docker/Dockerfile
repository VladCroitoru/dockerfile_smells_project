FROM multiarch/alpine:amd64-v3.6
MAINTAINER Guy Taylor <thebigguy.co.uk@gmail.com>

ARG VCS_REF
LABEL org.label-schema.vcs-ref=${VCS_REF} \
      org.label-schema.vcs-url="https://github.com/TheBiggerGuy/bfgminer-gridseed-docker"

COPY build.sh /build/build.sh
WORKDIR /build
RUN /build/build.sh && \
    rm -rf /build

ENTRYPOINT ["bfgminer"]
CMD ["--text-only"]
