FROM mmore500/conduit@sha256:8fdf051fb36163216e85bd0f162070a2224b2736874eee48bdd6fa1ace5efc99

USER root

COPY . /opt/signalgp-lite

RUN \
  apt-get update -qq \
    && \
  apt-get install -y --allow-downgrades --no-install-recommends \
    rename \
    && \
  apt-get clean \
    && \
  rm -rf /var/lib/apt/lists/* \
    && \
  echo "installed apt packages"

# install scripts associated with Python packages to /usr/local/bin
RUN \
  pip3 install --timeout 60 --retries 100 -r /opt/signalgp-lite/docs/requirements.txt \
    && \
  echo "installed Python packages"

# make sure unprivileged user has access to new files in opt
# adapted from https://stackoverflow.com/a/27703359
# and https://superuser.com/a/235398
RUN \
  chgrp --recursive user /opt/signalgp-lite \
    && \
  chmod --recursive g+rwx /opt/signalgp-lite \
    && \
  echo "user granted permissions to /opt/signalgp-lite"

USER user

# Define default working directory.
WORKDIR /opt/signalgp-lite

# must be installed as user for executable to be available on PATH
RUN \
  pip3 install --timeout 60 --retries 100 editorconfig-checker==2.3.54 \
    && \
  ln -s /home/user/.local/bin/ec /home/user/.local/bin/editorconfig-checker \
    && \
  echo "installed editorconfig-checker"

# adapted from https://askubuntu.com/a/799306
# and https://stackoverflow.com/a/38905161
ENV PATH "/home/user/.local/bin:$PATH"

RUN \
  make install-test-dependencies \
    && \
  echo "installed test dependencies"
