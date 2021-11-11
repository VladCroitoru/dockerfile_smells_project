ARG PYTHON_TAG=3.7.7-slim
FROM careerlist/python-app:${PYTHON_TAG}

ARG PYTHON_TAG
ARG NODE_VERSION=12.16.3
ARG GCLOUD_VERSION=293.0.0
ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.python-tag=${PYTHON_TAG} \
  org.label-schema.node-version=${NODE_VERSION} \
  org.label-schema.gcloud-version=${GCLOUD_VERSION} \
  org.label-schema.build-date=${BUILD_DATE} \
  org.label-schema.vcf-ref=${VCS_REF} \
  org.label-schema.URL="https://github.com/careerlist/python-node-gcloud" \
  maintainer="https://github.com/careerlist"

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
  && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 --no-same-owner \
  && rm "node-v$NODE_VERSION-linux-x64.tar.xz" \
  # cleanup
  && rm -rf /var/lib/apt/lists/* \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs

RUN npm install -g yarn && yarn global add bolt

ENV GOOGLE_DIR=/google \
  ADDITIONAL_COMPONENTS=beta

RUN mkdir -p ${GOOGLE_DIR} && cd ${GOOGLE_DIR} && apt-get update && apt-get install -y --no-install-recommends \
  # install CI tools
  jq \
  zip \
  lftp \
  openssh-client \
  coreutils \
  # install gcloud SDK
  && curl -SLO "https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${GCLOUD_VERSION}-linux-x86_64.tar.gz" \
  && tar -xzf "google-cloud-sdk-${GCLOUD_VERSION}-linux-x86_64.tar.gz" \
  && rm "google-cloud-sdk-${GCLOUD_VERSION}-linux-x86_64.tar.gz" \
  && google-cloud-sdk/install.sh --usage-reporting=false --path-update=false --bash-completion=false --additional-components ${ADDITIONAL_COMPONENTS} \
  && google-cloud-sdk/bin/gcloud config set --installation component_manager/disable_update_check true \
  && rm -rf google-cloud-sdk/.install/.backup \
  && rm -rf google-cloud-sdk/.install/.download \
  # install cloud_sql_proxy
  && curl -SLo cloud_sql_proxy -nv "https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64" \
  && chmod +x cloud_sql_proxy \
  && mkdir /cloudsql \
  # cleanup
  && rm -rf /var/lib/apt/lists/*

ENV PATH=${PATH}:${GOOGLE_DIR}:${GOOGLE_DIR}/google-cloud-sdk/bin

