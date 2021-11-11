FROM fedora:latest

LABEL maintainer="Ralph Bean" \
      summary="Image used to publish markdown to confluence." \
      distribution-scope="public"

RUN dnf install -y --setopt=tsflags=nodocs \
                python3-pip \
                pandoc \
                lua \
    && dnf clean all

COPY . /usr/local/.

# Always use the system CA.  There's no reason not to.
ENV REQUESTS_CA_BUNDLE=/etc/pki/tls/certs/ca-bundle.crt

RUN pip3 install --no-dependencies -r /usr/local/requirements.txt
