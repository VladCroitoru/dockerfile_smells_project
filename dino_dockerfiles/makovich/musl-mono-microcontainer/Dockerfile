FROM scratch

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

LABEL org.label-schema.build-date="$BUILD_DATE" \
      org.label-schema.name="musl-mono-microcontainer" \
      org.label-schema.description="Musl based Mono microcontainer POC" \
      org.label-schema.url="https://github.com/makovich/musl-mono-microcontainer" \
      org.label-schema.vcs-ref="$VCS_REF" \
      org.label-schema.vcs-url="https://github.com/makovich/musl-mono-microcontainer" \
      org.label-schema.version="$VERSION" \
      org.label-schema.schema-version="1.0" \
      org.label-schema.docker.cmd="docker run --rm -ti -p 5000:5000 makovich/musl-mono-microcontainer"

ADD artifacts/runtime.tar /

ENTRYPOINT ["/app"]
