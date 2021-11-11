FROM node:latest
MAINTAINER neshte

#Google Cloud SDK and Kubernetes
ENV GLUSTERVOLNAME data
ENV CLOUDSDK_PYTHON_SITEPACKAGES 1
RUN apt-get update && apt-get install -y -qq --no-install-recommends wget unzip python python-openssl openssh-client && apt-get clean \
    && wget https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.zip && unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip \
    && google-cloud-sdk/install.sh --usage-reporting=true --path-update=true --bash-completion=true --rc-path=/.bashrc --disable-installation-options \
    && yes | google-cloud-sdk/bin/gcloud components update kubectl \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
ENV PATH /google-cloud-sdk/bin:$PATH

COPY . /opt/neshte/gluster-k8s-sidecar

WORKDIR /opt/neshte/gluster-k8s-sidecar

RUN npm install

CMD ["npm", "start"]
