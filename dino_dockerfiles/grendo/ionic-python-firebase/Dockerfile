FROM beevelop/ionic

MAINTAINER grendo <grendo@gmail.com>

# Install Python, firebase
RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip python-virtualenv && \
  npm install --unsafe-perm -g firebase-tools && \
  rm -rf /var/lib/apt/lists/*
