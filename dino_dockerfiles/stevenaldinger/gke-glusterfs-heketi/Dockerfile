FROM alpine:3.6

ENV \
 CLOUDSDK_PYTHON_SITEPACKAGES="1" \
 # https://cloud.google.com/sdk/docs/release-notes
 CLOUD_SDK_VERSION="174.0.0" \
 GLUSTER_HEKETI_BOOTSTRAP_DIR="/gluster-heketi-bootstrap"

# makes commands available:
#     gcloud
#     kubectl
#     glusterfs-heketi-bootstrapper
#     gk-deploy
ENV PATH="/usr/bin/google-cloud-sdk/bin:/usr/bin/docker/docker:$GLUSTER_HEKETI_BOOTSTRAP_DIR/scripts/job:$GLUSTER_HEKETI_BOOTSTRAP_DIR/gluster-kubernetes/deploy:$PATH"

RUN apk add --no-cache \
          bash \
          curl \
          git \
 && apk add --no-cache \
          libc6-compat \
          openssh-client \
          py-crcmod \
          python \
 && curl -Lo /tmp/google-cloud-sdk.tar.gz "https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-$CLOUD_SDK_VERSION-linux-x86_64.tar.gz" \
 && tar xzfv /tmp/google-cloud-sdk.tar.gz -C /usr/bin/ \
 && rm /tmp/google-cloud-sdk.tar.gz \
 && gcloud config set core/disable_usage_reporting true \
 && gcloud config set component_manager/disable_update_check true \
 && gcloud components install kubectl \
 && mkdir -p "$GLUSTER_HEKETI_BOOTSTRAP_DIR/gluster-kubernetes" \
 && git clone https://github.com/gluster/gluster-kubernetes.git "$GLUSTER_HEKETI_BOOTSTRAP_DIR/gluster-kubernetes"

COPY . $GLUSTER_HEKETI_BOOTSTRAP_DIR/

WORKDIR $GLUSTER_HEKETI_BOOTSTRAP_DIR

CMD glusterfs-heketi-bootstrapper
