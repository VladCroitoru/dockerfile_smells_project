FROM golang:1.9.0

RUN go version

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
RUN wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | apt-key add -
RUN apt-get update && apt-get install -y build-essential \
    nodejs \
    sqlite3 \
    libsqlite3-dev \
    postgresql \
    postgresql-contrib \
    libpq-dev \
    mysql-client \
    vim \
    netcat \ 
    && rm -rf /var/lib/apt/lists/*
RUN go get -u github.com/golang/dep/cmd/dep
RUN npm install -g --no-progress yarn
RUN yarn config set yarn-offline-mirror /npm-packages-offline-cache
RUN yarn config set yarn-offline-mirror-pruning true

RUN go get -u -v github.com/gobuffalo/buffalo/buffalo
ENV BP=$GOPATH/src/github.com/gobuffalo/buffalo
WORKDIR $BP

ADD ./assets/wait-for /wait-for

# cache yarn packages to an offline mirror so they're faster to load. hopefully.
RUN grep -v '{{' $BP/generators/assets/webpack/templates/package.json.tmpl > package.json
RUN yarn install --no-progress

RUN buffalo version

WORKDIR $GOPATH/src

RUN ls -la /npm-packages-offline-cache

EXPOSE 3000
