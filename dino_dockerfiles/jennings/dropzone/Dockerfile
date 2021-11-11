FROM        ruby:2-alpine

WORKDIR     /app
COPY        ["Gemfile", "Gemfile.lock", "/app/"]

RUN         apk add --no-cache \
                ca-certificates \
                wget \
            && update-ca-certificates \
            && wget -q -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 \
            && chmod +x /usr/local/bin/dumb-init \
            && apk add --no-cache \
                make \
                gcc \
                g++ \
                libc-dev \
                sqlite-dev \
                postgresql-dev \
            && /usr/local/bin/gem install bundler \
            && bundle install --deployment --without development \
            && apk del \
                ca-certificates \
                wget \
                make \
                gcc \
                g++

COPY        [".", "/app/"]

VOLUME      ["/data"]
EXPOSE      8000
ENV         DATABASE_URL=sqlite3:///data/dropzone.sqlite3
ENTRYPOINT  ["/usr/local/bin/dumb-init", "--"]
CMD         ["/usr/local/bin/bundle", "exec", "rackup", "--env", "deployment", "--host", "0.0.0.0", "--port", "8000"]
