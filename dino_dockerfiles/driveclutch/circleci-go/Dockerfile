FROM golang:1.16.3

RUN apt-get update \
    && apt-get install -y \
	  openssh-client \
	  ca-certificates \
	  tar \
	  gzip zip \
	  python-pip \
	  lsb-release  shellcheck bats \
    && go get github.com/jstemmer/go-junit-report \
    && go get honnef.co/go/tools/cmd/staticcheck \
    && export DOCKER_VERSION=$(curl --silent --fail --retry 3 https://download.docker.com/linux/static/stable/x86_64/ | grep -o -e 'docker-[.0-9]*-ce\.tgz' | sort -r | head -n 1) \
    && DOCKER_URL="https://download.docker.com/linux/static/stable/x86_64/${DOCKER_VERSION}" \
    && echo Docker URL: $DOCKER_URL \
    && curl --silent --show-error --location --fail --retry 3 --output /tmp/docker.tgz "${DOCKER_URL}" \
    && ls -lha /tmp/docker.tgz \
    && tar -xz -C /tmp -f /tmp/docker.tgz \
    && mv /tmp/docker/* /usr/bin \
    && rm -rf /tmp/docker /tmp/docker.tgz linux-amd64 \
    && pip install --upgrade awscli

COPY tools/* /tools/
