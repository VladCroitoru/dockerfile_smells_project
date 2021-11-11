FROM buildpack-deps:jessie-curl
LABEL maintainer "matt urbanski (https://keybase.io/iflowfor8hours)"

RUN \
  apt-get update && apt-get install -y \
    fuse \
    libappindicator1 \
    gnupg \
    haveged \
    git-core \
    vim-nox \
    ssh-client \
    --no-install-recommends \

  # Get and verify Keybase.io's code signing key
  && curl https://keybase.io/docs/server_security/code_signing_key.asc | \
  gpg --import \
  && gpg --fingerprint 222B85B0F90BE2D24CFEB93F47484E50656D16C7 \

  # Get, verify and install client package
  && curl -O https://prerelease.keybase.io/keybase_amd64.deb.sig \
  && curl -O https://prerelease.keybase.io/keybase_amd64.deb \
  && gpg --verify keybase_amd64.deb.sig keybase_amd64.deb \
  && dpkg -i keybase_amd64.deb \
  && apt-get install -f \

  # Create group, user
  && groupadd -g 1000 keybase \
  && useradd --create-home -g keybase -u 1000 keybase \
  && mkdir /root/.ssh \

  # Install gcredstash
  && wget https://github.com/winebarrel/gcredstash/releases/download/v0.3.1/gcredstash_0.3.1_amd64.deb \
  && dpkg -i gcredstash_0.3.1_amd64.deb \
  && alias gcredstash=credstash \

  # Install blackbox
  && wget https://github.com/StackExchange/blackbox/archive/production.tar.gz \
  && tar xzvf production.tar.gz -C /usr/bin --strip-components=2 blackbox-production/bin/ \

  # Cleanup
  && rm -r /var/lib/apt/lists/* \
  && rm keybase_amd64.deb* \
  && rm gcredstash_0.3.1_amd64.deb \
  && rm production.tar.gz

ENV AWS_ACCESS_KEY_ID=
ENV AWS_SECRET_ACCESS_KEY=
ENV AWS_REGION=us-east-1

USER keybase
WORKDIR /home/keybase
CMD ["bash"]

RUN run_keybase
