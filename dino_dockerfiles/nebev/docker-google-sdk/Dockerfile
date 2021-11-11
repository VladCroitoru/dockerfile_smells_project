FROM google/cloud-sdk

RUN apt-get update && apt-get install -y \
     apt-transport-https \
     ca-certificates \
     curl \
     software-properties-common \
     && rm -rf /var/lib/apt/lists/* \
     && curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -

RUN add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"

RUN apt-get update && apt-get install -y docker-ce && rm -rf /var/lib/apt/lists/*

