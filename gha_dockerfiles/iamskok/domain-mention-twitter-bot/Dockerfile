FROM node:17.0.1-alpine3.12

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn install --production

COPY . ./

ARG CLOUD_SDK_VERSION=319.0.0
ENV CLOUD_SDK_VERSION=$CLOUD_SDK_VERSION
ENV PATH /root/google-cloud-sdk/bin:$PATH
ENV FIREBASE_ADMIN_SDK_CREDENTIALS=/app/service-account/firebase-adminsdk.json

RUN apk --no-cache add \
        curl \
        python3 \
        py3-crcmod \
        bash \
        libc6-compat \
        openssh-client \
        git \
        gnupg \
    && cd /root \
    && curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz \
    && tar xzf google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz \
    && rm google-cloud-sdk-${CLOUD_SDK_VERSION}-linux-x86_64.tar.gz

CMD gcloud auth activate-service-account --key-file="${FIREBASE_ADMIN_SDK_CREDENTIALS}" \
  && export GOOGLE_APPLICATION_CREDENTIALS="${FIREBASE_ADMIN_SDK_CREDENTIALS}" \
  && yarn start
