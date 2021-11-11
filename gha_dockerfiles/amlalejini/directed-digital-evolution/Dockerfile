FROM devosoft/empirical

USER root

COPY . /opt/directed-digital-evolution

RUN \
  pip3 install -r /opt/directed-digital-evolution/docs/requirements.txt \
    && \
  echo "installed documentation build requirements"

RUN \
  find /etc/apt -type f -name '*.list' -exec sed -i 's/^# \(deb.*-backports.*\)/\1/; s/^# \(deb.*-updates.*\)/\1/; s/^# \(deb.*-proposed.*\)/\1/; s/^# \(deb.*-security.*\)/\1/' {} + \
    && \
  add-apt-repository -y ppa:ubuntu-toolchain-r/test \
    && \
  wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
    && \
  apt-add-repository "deb https://apt.llvm.org/xenial/ llvm-toolchain-xenial-7 main" \
    && \
  apt-get update -qq \
    && \
  apt-get install -y cmake build-essential python-virtualenv python-pip nodejs tar gzip libclang-7-dev llvm-7 llvm-7-dev clang-7 libstdc++-7-dev gdb \
    && \
  update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-7 90 \
    && \
  update-alternatives --install /usr/bin/llvm-config llvm-config /usr/bin/llvm-config-7 90 \
    && \
  update-alternatives --install /usr/bin/llvm-profdata llvm-profdata /usr/bin/llvm-profdata-7 90 \
    && \
  update-alternatives --install /usr/bin/llvm-cov llvm-cov /usr/bin/llvm-cov-7 90 \
    && \
  echo "installed force cover build dependencies"

# make sure unprivileged user has access to new files in opt
# adapted from https://stackoverflow.com/a/27703359
# and https://superuser.com/a/235398
RUN \
  chgrp --recursive user /opt/directed-digital-evolution \
    && \
  chmod --recursive g+rwx /opt/directed-digital-evolution \
    && \
  echo "user granted permissions to /opt/directed-digital-evolution"

USER user

RUN \
  cd /opt/directed-digital-evolution \
    && \
  make install-test-dependencies \
    && \
  echo "installed test dependencies"

# Define default working directory.
WORKDIR /opt/directed-digital-evolution
