# Cannot use focal since cloud sdk not released for it yet.
# See: https://packages.cloud.google.com/apt/dists => cloud-sdk-*
FROM ubuntu:bionic
MAINTAINER Grow SDK Authors <hello@grow.io>

# Set environment variables.
ENV TERM=xterm
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=US/Pacific

# Update system.
RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y --no-install-recommends \
    software-properties-common curl ca-certificates gpg-agent \
    pylint build-essential zip libc6 libyaml-dev libffi-dev \
    libxml2-dev libxslt-dev libssl-dev git ssh \
  && add-apt-repository ppa:deadsnakes/ppa \
  && curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - \
  && echo "deb http://packages.cloud.google.com/apt cloud-sdk-$(lsb_release -c -s) main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
  && curl -sL https://deb.nodesource.com/setup_12.x | bash - \
  && add-apt-repository ppa:longsleep/golang-backports \
  && apt-get update \
  && apt-get install -y --no-install-recommends golang-go google-cloud-sdk \
    google-cloud-sdk-app-engine-python nodejs \
    python3.8 python3-pip python3-setuptools python3-all-dev python3-dev \
  && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1 \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Add to path.
ENV PATH=$PATH:/usr/lib/go-1.13/bin
ENV PYTHONPATH="${PYTHONPATH}:/usr/lib/google-cloud-sdk/platform/google_appengine"
ENV GOPATH=$HOME/gocode
ENV PATH=$PATH:$GOPATH/bin

# Update pip.
RUN pip3 install --upgrade pip virtualenv pipenv

# Install NPM globals.
RUN npm install -g gulp yarn

# Install github release uploader.
RUN go get -u github.com/tcnksm/ghr

# Confirm versions that are installed.
RUN echo "Node: `node -v`" \
  && echo "NPM: `npm -v`" \
  && echo "Yarn: `yarn --version`" \
  && echo "Gulp: `gulp -v`" \
  && echo "GCloud: `gcloud -v`" \
  && echo "Yarn: `yarn --version`" \
  && echo "Go: `go version`" \
  && echo "GHR: `ghr --version`" \
  && echo "Python 3: `python3 --version`" \
  && echo "Python 3: `pip3 --version`"
