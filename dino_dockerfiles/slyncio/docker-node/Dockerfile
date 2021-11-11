# use node:8-slim as base image
FROM node:8-slim

# install docker, node, gcloud sdk
ENV DOCKER_VERSION 17.12.0~ce-0~debian
RUN apt-get update \
    && apt-get -y install \
      apt-transport-https \
      ca-certificates \
      curl \
      gnupg2 \
      software-properties-common \
      jq \
      git \
      zsh \
    && curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | apt-key add - \
    && apt-key fingerprint 0EBFCD88 \
    && add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") \
   $(lsb_release -cs) \
   stable" \
   && apt-get update \
   && apt-get -y install docker-ce=${DOCKER_VERSION} \
   && rm -rf /var/cache/apt \
   && npm install -g npm

# below files are taken from docker's own image
# see here: https://github.com/docker-library/docker/tree/master/17.12
# see license DOCKER-LICENSE
COPY modprobe.sh /usr/local/bin/modprobe
COPY docker-entrypoint.sh /usr/local/bin/

# add a new user
# RUN useradd -u 1001 -s /bin/zsh -m dev
# USER dev
# WORKDIR /home/dev

# install gcloud
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-274.0.1-linux-x86_64.tar.gz -nv \
   && tar zxf google-cloud-sdk-274.0.1-linux-x86_64.tar.gz \
   && ./google-cloud-sdk/install.sh --usage-reporting=false --path-update=true \
   && ./google-cloud-sdk/bin/gcloud --quiet components update \
   && ./google-cloud-sdk/bin/gcloud components install docker-credential-gcr \
   && rm -rf ./google-cloud-sdk/.install
ENV PATH "${PATH}:${PWD}/google-cloud-sdk/bin"

# install ohmyzsh
# RUN sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"

# the entry point script is needed mainly
# to support use of docker:dind
ENTRYPOINT ["docker-entrypoint.sh"]
CMD [ "node" ]
