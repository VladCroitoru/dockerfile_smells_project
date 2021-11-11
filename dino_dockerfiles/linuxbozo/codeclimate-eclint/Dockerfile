FROM node:6.10-slim
LABEL maintainer "M. Adam Kendall <linuxbozo@gmail.com>"

RUN apt-key adv --fetch-keys http://dl.yarnpkg.com/debian/pubkey.gpg && \
    echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update

WORKDIR /usr/src/app
COPY engine.json package.json yarn.lock ./

RUN apt-get install -y git jq yarn && \
    yarn install && \
    version="v$(npm -j ls eclint | jq -r .dependencies.eclint.version)" && \
    cat engine.json | jq ".version = \"$version\"" > /engine.json && \
    apt-get purge -y git jq yarn && \
    apt-get autoremove --yes

RUN adduser --uid 9000 --gecos "" --disabled-password app
COPY . ./
RUN chown -R app:app ./

USER app

VOLUME /code
WORKDIR /code

CMD ["/usr/src/app/bin/eclint"]
