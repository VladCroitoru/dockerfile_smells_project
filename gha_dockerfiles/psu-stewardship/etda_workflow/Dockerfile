# syntax=docker/dockerfile:experimental
FROM ruby:2.6.6 as base

## NodeJS
ENV NODE_VERSION 12.22.3
RUN mkdir /usr/local/nvm
ENV NVM_DIR /usr/local/nvm
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

### Envconsul
RUN curl -Lo /tmp/envconsul.zip https://releases.hashicorp.com/envconsul/0.9.2/envconsul_0.9.2_linux_amd64.zip && \
    unzip /tmp/envconsul.zip -d /bin && \
    rm /tmp/envconsul.zip

RUN . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

RUN npm install -g yarn@1.19.1

# Clam AV 
RUN apt-get update && \ 
  apt-get install --no-install-recommends mariadb-client clamav clamdscan clamav-daemon wget libpng-dev make -y && \
  rm -rf /var/lib/apt/lists/*

RUN mkdir /var/run/clamav && \
    chown clamav:clamav /var/run/clamav && \
    chmod 750 /var/run/clamav

RUN touch  /etc/clamav/clamd.conf

RUN curl -Lo /var/lib/clamav/main.cvd http://database.clamav.net/main.cvd && \
    curl -Lo /var/lib/clamav/daily.cvd http://database.clamav.net/daily.cvd && \
    curl -Lo /var/lib/clamav/bytecode.cvd http://database.clamav.net/bytecode.cvd && \
    chown clamav:clamav /var/lib/clamav/*.cvd && \
    chown clamav:clamav /var/log/clamav/*

RUN chmod g+w /var/lib/clamav
  
RUN sed -i 's/^Foreground .*$/Foreground true/g' /etc/clamav/clamd.conf && \
    echo "TCPSocket 3310" >> /etc/clamav/clamd.conf && \
    sed -i 's/^Foreground .*$/Foreground true/g' /etc/clamav/freshclam.conf

ENV TZ=America/New_York

WORKDIR /etda_workflow

COPY bin/vaultshell /usr/local/bin/

COPY Gemfile Gemfile.lock /etda_workflow/

ARG SSH_PRIVATE_KEY
ARG RAILS_ENV
ENV RAILS_ENV=$RAILS_ENV
ENV SSH_PRIVATE_KEY_ENV=$SSH_PRIVATE_KEY

RUN useradd -u 10000 etda -d /etda_workflow
RUN usermod -G clamav etda
RUN mkdir -p /etda_workflow/.ssh
RUN chown -R etda /etda_workflow
RUN chown -R etda /etda_workflow/.ssh

USER etda
RUN gem install bundler:2.0.2
COPY --chown=etda vendor/ vendor/
RUN bundle install --path vendor/bundle

COPY yarn.lock /etda_workflow
COPY package.json /etda_workflow
RUN yarn

COPY --chown=etda . /etda_workflow

RUN mkdir -p tmp/cache

CMD ["./entrypoint.sh"]

USER root
RUN chmod -R 775 /var/log/clamav
RUN chmod -R 775 /var/run/clamav
USER etda

FROM base as rspec
CMD ["/etda_workflow/bin/ci-rspec"]

FROM base as production

RUN bundle install --without development test

RUN PARTNER=graduate RAILS_ENV=production DEVISE_SECRET_KEY=$(bundle exec rails secret) bundle exec rails assets:precompile

CMD ["./entrypoint.sh"]

