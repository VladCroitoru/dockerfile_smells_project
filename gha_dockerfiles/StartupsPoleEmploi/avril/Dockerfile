FROM elixir:1.8.2

RUN apt-get update
RUN apt-get install --fix-missing -y \
    sshpass \
    inotify-tools \
    libfontenc1 \
    libxfont1 \
    xfonts-encodings \
    xfonts-utils \
    xfonts-base \
    xfonts-75dpi \
    # apt-transport-https \
    # ca-certificates \
    postgresql-client

# Install wkhtmltopdf
RUN wget -P /root https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.stretch_amd64.deb
RUN dpkg -i /root/wkhtmltox_0.12.6-1.stretch_amd64.deb || true

# Install goon
RUN wget -P /root https://github.com/alco/goon/releases/download/v1.1.1/goon_linux_amd64.tar.gz
RUN tar -C /root -vxf /root/goon_linux_amd64.tar.gz
RUN mv /root/goon /usr/local/bin/

# Install node
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update
RUN apt-get install -y nodejs
RUN apt-get install -y --no-install-recommends yarn

RUN mkdir -p /app

ADD ./mix.exs /app/mix.exs
ADD ./mix.lock /app/mix.lock
COPY ./assets/package.json ./assets/yarn.lock* /app/assets/
# ADD assets/package-lock.json /app/assets/package-lock.json
# ADD assets/yarn.lock /app/assets/yarn.lock

WORKDIR /app

# Install dependencies
RUN mix local.hex --force
RUN mix local.rebar --force
RUN mix deps.get
RUN yarn --cwd ./assets install

# Install min.io client
RUN wget -nv -P /usr/bin https://dl.min.io/client/mc/release/linux-amd64/mc
RUN chmod +x /usr/bin/mc

# Setup DB
# RUN mix ecto.create && mix ecto.migrate # Note: run once the db is connected
# RUN mix run priv/repo/seeds.exs