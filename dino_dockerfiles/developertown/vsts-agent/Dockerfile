FROM ubuntu:16.04

# install vsts pre-reqs and basic build environment items
RUN \
     apt-get update \
  #  Setup apt for the git PPA and to get docker from their source repo \
  && apt-get install -y software-properties-common python-software-properties \
  && apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D \
  && echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" > /etc/apt/sources.list.d/docker.list \
  && add-apt-repository ppa:git-core/ppa \
  && apt-get install -y curl apt-transport-https \
  && apt-get update \
  #  Install vsts pre-reqs and docker \
  && apt-get install -y \
       ca-certificates \
       libunwind8 \
       libcurl3 \
       build-essential \
       git \
       iputils-ping \
       docker-engine \
   # Useful packages for dev needs: \
       openssl \
       libreadline6 \
       libreadline6-dev \
       zlib1g zlib1g-dev \
       libssl-dev libyaml-dev \
       libsqlite3-dev \
       sqlite3 \
       libxml2-dev \
       libxslt-dev \
       autoconf \
       libc6-dev \
       automake \
       default-jdk \
  #  clean up and install vsts agent \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && adduser \
       --disabled-password \
       --home /usr/local/vsts-agent \
       --shell /bin/bash \
       --gecos "VSTS Agent" \
       --ingroup docker \
       vsts

ENV \
    VSTS_VERSION="2.107.0" \
    AGENT_FLAVOR=Generic \
    PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

WORKDIR /usr/local/vsts-agent

RUN \
     curl -Ls https://github.com/Microsoft/vsts-agent/releases/download/v${VSTS_VERSION}/vsts-agent-ubuntu.16.04-x64-${VSTS_VERSION}.tar.gz \
   | tar xvzf - \
  && mkdir /usr/local/vsts-agent/_work

# Copy in and run custom start wrapper
COPY start.sh ./
RUN chown -R vsts:docker /usr/local/vsts-agent

USER vsts
CMD /usr/local/vsts-agent/start.sh
