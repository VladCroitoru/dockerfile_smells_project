FROM docker:git

MAINTAINER Marcus Welz <marcus@swiftchase.com>

# We want Google's Cloud SDK, which requires Python,
# and kubectl, which we'll install via gcloud.

RUN apk update \
    && apk add ca-certificates wget \
    && update-ca-certificates \
    && mkdir /opt \
    && cd /opt \
    && wget -q https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-202.0.0-linux-x86_64.tar.gz \
    && tar -xzf google-cloud-sdk-202.0.0-linux-x86_64.tar.gz \
    && rm google-cloud-sdk-202.0.0-linux-x86_64.tar.gz \
    && ln -s /opt/google-cloud-sdk/bin/gcloud /usr/bin/gcloud \
    && apk -q add python \
    && apk add --update libintl \
    && apk add --virtual build_deps gettext \
    && cp /usr/bin/envsubst /usr/local/bin/envsubst \
    && apk del build_deps \
    && rm -rf /var/cache/apk/* \
    && echo "y" | gcloud components install kubectl \
    && ln -s /opt/google-cloud-sdk/bin/kubectl /usr/bin/kubectl
