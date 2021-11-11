FROM scratch

ARG BUILD_DIR
ARG BINARY_NAME

COPY $BUILD_DIR/$BINARY_NAME /service

EXPOSE 80 81 10000 10001
CMD ["/service"]
HEALTHCHECK --interval=2m --timeout=3s CMD curl -f http://localhost:10000/healthz || exit 1
