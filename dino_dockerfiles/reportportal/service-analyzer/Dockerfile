FROM alpine:3.7

LABEL maintainer="Andrei Varabyeu <andrei_varabyeu@epam.com>"
LABEL version=5.0.0

ENV APP_DOWNLOAD_URL https://dl.bintray.com/epam/reportportal/5.0.0

ADD ${APP_DOWNLOAD_URL}/service-analyzer_linux_amd64 /service-analyzer

RUN chmod +x /service-analyzer && \
    apk add --no-cache ca-certificates

EXPOSE 8080
ENTRYPOINT ["/service-analyzer"]
