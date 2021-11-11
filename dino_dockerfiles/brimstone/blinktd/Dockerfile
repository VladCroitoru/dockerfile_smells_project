ARG REPOSITORY=github.com/brimstone/blinktd
ARG CGO_ENABLED=0
FROM brimstone/golang as builder
RUN echo GOARCH: ${GOARCH}

FROM scratch

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/brimstone/blinktd" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="1.0.0-rc1"

COPY --from=builder /app /blinktd

ENTRYPOINT ["/blinktd"]
CMD ["serve"]
