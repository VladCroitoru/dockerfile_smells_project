FROM mhart/alpine-node:7.1.0

COPY ./setup.js /usr/bin/container-setup/setup
COPY ./package.json /usr/bin/container-setup/package.json
COPY ./bash_shell /usr/bin/bash_shell
COPY ./container_start /usr/bin/container_start

RUN apk add --no-cache bash git curl make python-dev py-pip python build-base openssh openssl\
&& npm install -g triton manta json \
&& cd ~ \
&& mkdir .ssh \
&& curl -O https://manta.bne.blenco.net.au/davefinster/public/gitlab-runner-helper \
&& mv gitlab-runner-helper /usr/bin/gitlab-runner-helper \
&& chmod +x /usr/bin/gitlab-runner-helper \
&& curl -O https://get.docker.com/builds/Linux/x86_64/docker-latest.tgz \
&& curl -L https://github.com/docker/machine/releases/download/v0.8.2/docker-machine-`uname -s`-`uname -m` > /usr/bin/docker-machine \
&& chmod +x /usr/bin/docker-machine \
&& tar -zxvf docker-latest.tgz \
&& mv docker/docker /usr/bin/docker \
&& chmod +x /usr/bin/docker \
&& rm -rf docker \
&& mkdir -p ~/.triton/profiles.d \
&& chmod +x /usr/bin/container-setup/setup \
&& cd /usr/bin/container-setup \
&& npm install \
&& chmod +x /usr/bin/bash_shell \
&& chmod +x /usr/bin/container_start \
&& pip install --upgrade docker-compose==1.7.0 \
&& cd /etc \
&& curl -O https://curl.haxx.se/ca/cacert.pem 

ENV CURL_CA_BUNDLE=/etc/cacert.pem

ENTRYPOINT [ "/usr/bin/container_start"]