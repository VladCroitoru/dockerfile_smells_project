FROM ruby:2.6.5

RUN mkdir -p /workspace

WORKDIR /workspace

COPY install /install

# Install node required by locomotive and many project
RUN DEBIAN_FRONTEND=noninteractive \
    && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list\
    && apt-get update \
    && apt-get install -y nodejs vim mongo-tools yarn\
    && /install/gosu.sh \
    && apt-get clean

COPY stack/entrypoint /usr/local/bin/entrypoint
COPY stack/bash_aliases /stack/bash_aliases

ENV LANG C.UTF-8
ENTRYPOINT ["/usr/local/bin/entrypoint"]
EXPOSE 3000
EXPOSE 3333
