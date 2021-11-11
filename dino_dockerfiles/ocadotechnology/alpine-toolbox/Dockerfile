FROM gcr.io/google-containers/exechealthz-amd64:v1.2.0

USER root:root
RUN apk add --no-cache curl \
                       wget \
                       netcat-openbsd \
                       socat \
                       bind-tools \
                       tcpdump \
                       bash

ENTRYPOINT ["/bin/bash"]
