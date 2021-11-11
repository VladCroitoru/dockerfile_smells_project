FROM google/cloud-sdk

ENV HUGO_VERSION=0.37.1
ENV HUGO_DOWNLOAD_URL=https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz

RUN apt-get update
RUN apt-get install -y \
    git \
    wget

RUN wget "$HUGO_DOWNLOAD_URL" && \
    tar xzf hugo_${HUGO_VERSION}_Linux-64bit.tar.gz && \
	mv hugo /usr/bin/hugo && \
    rm hugo_${HUGO_VERSION}_Linux-64bit.tar.gz LICENSE.md README.md

EXPOSE 1313
