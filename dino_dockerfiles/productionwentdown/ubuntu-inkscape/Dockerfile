FROM        ubuntu

MAINTAINER  serverwentdown

RUN         apt-get update \
            && apt-get install -y openssl wget zip unzip tar xz-utils gzip openssh-client git jq inkscape \
            && wget -O /tmp/index.json https://nodejs.org/dist/index.json \
            && VER=$(cat /tmp/index.json | jq -r '.[0].version') \
            && rm /tmp/index.json \
            && wget -O /tmp/node.tar.xz https://nodejs.org/dist/$VER/node-$VER-linux-x64.tar.xz \
            && tar -C /usr/local --strip-components 1 -xvf /tmp/node.tar.xz \
            && apt-get clean && rm -rf /var/lib/apt/lists/*

CMD         ["/bin/bash"]
