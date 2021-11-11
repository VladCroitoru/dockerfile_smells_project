FROM python:3.7-slim-stretch

ENV PYTHON_VERSION=3.7.9

RUN set -ex; \
  \
  echo "deb http://deb.debian.org/debian stretch-backports main" > /etc/apt/sources.list.d/debian-backports.list; \
  apt-get update; \
  apt-get install -y --no-install-recommends \
  libxslt1-dev \
  libxml2 \
  libsm6 \
  libxext6 \
  libglib2.0-0 \
  build-essential \
  g++ \
  gcc \
  git \
  libffi-dev \
  libssl-dev \
  default-libmysqlclient-dev \
  libpq-dev \
  zlib1g-dev \
  libbz2-dev \
  libreadline-dev \
  libsqlite3-dev \
  wget \
  llvm \
  libncurses5-dev \
  libncursesw5-dev \
  xz-utils \
  tk-dev \
  liblzma-dev \
  python-openssl \
  unzip \
  ssh \
  curl; \
  apt-get -t stretch-backports -y --no-install-recommends install git; \
  rm -rf /var/lib/apt/lists/*;

# Sigh, needed to pin docker version
RUN export DOCKER_VERSION=docker-19.03.8.tgz \
  && DOCKER_URL="https://download.docker.com/linux/static/stable/x86_64/${DOCKER_VERSION}" \
  && echo Docker URL: $DOCKER_URL \
  && curl --silent --show-error --location --fail --retry 3 --output /tmp/docker.tgz "${DOCKER_URL}" \
  && ls -lha /tmp/docker.tgz \
  && tar -xz -C /tmp -f /tmp/docker.tgz \
  && mv /tmp/docker/* /usr/bin \
  && rm -rf /tmp/docker /tmp/docker.tgz \
  && which docker \
  && (docker version || true) \
  && pip install --ignore-installed -U pip setuptools \
  && cd /opt && curl --insecure -OL https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.2.0.1873-linux.zip \
  && unzip sonar-scanner-cli-4.2.0.1873-linux.zip && rm sonar-scanner-cli-4.2.0.1873-linux.zip \
  && ln -s /opt/sonar-scanner-4.2.0.1873-linux/bin/sonar-scanner /usr/bin/

WORKDIR /root

RUN git clone https://github.com/pyenv/pyenv.git .pyenv

RUN git clone https://github.com/pyenv/pyenv-virtualenv.git .pyenv/plugins/pyenv-virtualenv 

RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> .bashrc && \
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> .bashrc && \
  echo 'eval "$(pyenv init -)"' >> .bashrc && \
  echo 'eval "$(pyenv virtualenv-init -)"' >> .bashrc

RUN /bin/bash -c "source .bashrc && pyenv install -s ${PYTHON_VERSION}"
