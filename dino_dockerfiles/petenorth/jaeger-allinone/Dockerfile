FROM jaegertracing/all-in-one
USER 10001
CMD ["/go/bin/standalone-linux","--span-storage.type=memory","--query.static-files=/go/src/jaeger-ui-build/build/"]
