FROM alpine
MAINTAINER Marcelo Almeida <ms.almeida86@gmail.com>

ADD https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-amd64 /bin/confd
RUN chmod a+x /bin/confd

VOLUME ["/etc/docker/registry/"]

ADD etc/confd/ /etc/confd/

ENV \
  STORAGE_S3_ACCESSKEY="" \
  STORAGE_S3_SECRETKEY="" \
  STORAGE_S3_REGION="" \
  STORAGE_S3_BUCKET="" \
  STORAGE_S3_ENCRYPT="true" \
  STORAGE_S3_SECURE="true" \
  STORAGE_S3_V4AUTH="true" \
  STORAGE_S3_CHUNKSIZE="5242880" \
  STORAGE_S3_ROOTDIRECTORY="/" \
  STORAGE_DELETE_ENABLED="false" \
  STORAGE_CACHE_BLOBDESCRIPTOR="inmemory" \
  HTTP_ADDR=":5000" \
  HTTP_TLS_CERTIFICATE="" \
  HTTP_TLS_KEY="" \
  REPORTING_NEWRELIC_LICENSEKEY="" \
  REPORTING_NEWRELIC_NAME="" \
  REPORTING_NEWRELIC_VERBOSE="false"

CMD /bin/confd -onetime -backend=env

