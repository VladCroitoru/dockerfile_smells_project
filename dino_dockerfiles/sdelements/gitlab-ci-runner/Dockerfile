FROM python:3.6-stretch

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update \
  && apt-get -y install apt-transport-https wget \
  && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
  && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
  && apt-get -y update \
  && curl -sL https://deb.nodesource.com/setup_14.x | bash - \
  && echo "Package: nodejs" >> /etc/apt/preferences.d/nodejs \
  && echo "Pin: version 14*" >> /etc/apt/preferences.d/nodejs \
  && echo "Pin-Priority: 550" >> /etc/apt/preferences.d/nodejs \
  && apt-get -y install virtualenv sendmail-bin sendmail krb5-config krb5-user python-ldap libsasl2-dev python3-dev libldap2-dev libssl-dev xmlsec1 libfontconfig nodejs yarn vagrant openssh-client jq bsdmainutils unzip vim postgresql xfonts-75dpi xfonts-base xfonts-utils \
  && wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.stretch_amd64.deb \
  && dpkg -i wkhtmltox_0.12.5-1.stretch_amd64.deb \
  # Libcairo
  && apt-get -y install build-essential python-cffi libcairo2 libpango1.0-0 libpangocairo-1.0.0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info \
  # Cypress
  && apt-get -y install libgtk2.0-0 libgtk-3-0 libgbm-dev libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2 libxtst6 xauth xvfb \
  && npm install -g grunt-cli \
  && sed -i 's/peer$/trust/g; s/md5$/trust/g' $(find /etc/postgresql -name pg_hba.conf) \
  && service postgresql restart \
  && curl -fsSL get.docker.com | sh \
  && curl -L https://github.com/docker/compose/releases/download/1.27.4/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \
  && chmod +x /usr/local/bin/docker-compose \
  && wget 'https://github.com/koalaman/shellcheck/releases/download/latest/shellcheck-latest.linux.x86_64.tar.xz' \
  && xz -d ./shellcheck-latest.linux.x86_64.tar.xz \
  && tar -xvf ./shellcheck-latest.linux.x86_64.tar \
  && cp ./shellcheck-latest/shellcheck /usr/bin/ \
  && chmod 755 /usr/bin/shellcheck \
  && rm -rf /var/lib/apt/lists/*
