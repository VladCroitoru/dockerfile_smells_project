FROM alpine
WORKDIR /app/
RUN  apk add --no-cache curl tzdata
ADD forseti .
ENV GIN_MODE=release \
    PORT=8080 \
    FORSETI_JSON_LOG=1 \
    FORSETI_LOG_LEVEL=info
CMD ["./forseti"]
HEALTHCHECK --interval=10s --timeout=3s CMD curl -f http://localhost:8080/status || exit 1
