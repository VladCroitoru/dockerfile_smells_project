FROM elixir:1.5.3

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN \
  apt-get update && \
  apt-get install -y apt-utils && \
  apt-get upgrade -y && \
  apt-get install -y inotify-tools && \
  curl -sL https://deb.nodesource.com/setup_7.x | bash - && \
  apt-get install -y nodejs && \
  apt-get clean && \
  cd /var/lib/apt/lists && rm -fr *Release* *Sources* *Packages* && \
  truncate -s 0 /var/log/*log

ENV PHOENIX_VERSION ""

RUN \
  echo "Phoenix 1.3.0" && \
  mix local.hex --force && \
  mix local.rebar --force && \
  mix archive.install --force https://github.com/phoenixframework/archives/raw/master/phx_new.ez

ENV MYAPP_DIR "/myapp"
ENV MIX_ENV "prod"

CMD ["iex"]
