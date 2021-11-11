FROM        ubuntu

MAINTAINER  serverwentdown

RUN         apt-get update \
            && apt-get install -y openssl wget zip unzip tar xz-utils gzip openssh-client git \
            && apt-get clean && rm -rf /var/lib/apt/lists/*

CMD         ["/bin/bash"]
