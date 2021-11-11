FROM registry.access.redhat.com/ubi8/ubi-minimal:latest

LABEL maintainer="adorsys GmbH & Co. KG" \
      vendor="adorsys GmbH & Co. KG" \
      name="adorsys/s3-tools" \
      org.label-schema.vendor="adorsys GmbH & Co. KG" \
      org.label-schema.name="adorsys/s3-tools" \
      io.k8s.display-name="adorsys/s3-tools" \
      summary="adorsys/s3-tools" \
      io.k8s.description="adorsys/s3-tools" \
      org.label-schema.description="adorsys/s3-tools" \
      org.label-schema.schema-version="1.0" \
      org.label-schema.usage="" \
      org.label-schema.license="" \
      org.label-schema.build-date=""

ENV PAGER="more" HOME=/tmp

COPY --from=minio/mc:latest /usr/bin/mc /usr/bin/mc

# Install util-linux for commands like mountpoint
RUN microdnf install -y procps-ng curl util-linux findutils python3 python3-pip \
  && microdnf clean all \
  && pip3 --disable-pip-version-check install -U --compile --no-cache-dir awscli s3cmd
