FROM ubuntu:focal
LABEL maintainer="jay@outfielding.net"
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends \
    apt-utils \
    file \
    openssh-client \
    locales \
    software-properties-common \
    rsyslog \
    sudo \
    iproute2 \
    curl \
    openssl \
    libssl-dev \
    libffi-dev \
    git
RUN apt-get install -y ruby ruby-dev
RUN apt-get install -y  python3 python3-setuptools python3-pip python-is-python3

ENV KUBE_LATEST_VERSION="v1.21.1"

RUN curl -L https://storage.googleapis.com/kubernetes-release/release/${KUBE_LATEST_VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
 && chmod +x /usr/local/bin/kubectl

RUN rm -Rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean

# Fix potential UTF-8 errors with ansible-test.
RUN locale-gen en_US.UTF-8

# Remove unnecessary getty and udev targets that result in high CPU usage when using
# multiple containers with Molecule (https://github.com/ansible/molecule/issues/1104)
RUN rm -f /lib/systemd/system/systemd*udev* \
  && rm -f /lib/systemd/system/getty.target

WORKDIR /tmp

ADD Gemfile Gemfile
ADD Gemfile.lock Gemfile.lock
RUN gem install bundler && bundle install

RUN pip3 install pipenv
ADD Pipfile Pipfile
ADD Pipfile.lock Pipefile.lock
RUN pipenv install
