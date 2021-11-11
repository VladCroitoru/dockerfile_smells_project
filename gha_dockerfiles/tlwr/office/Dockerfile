ARG ruby_version

# https://tailscale.com/kb/1107/heroku/
FROM alpine:latest as tailscale
WORKDIR /app
COPY . ./
ENV TSFILE=tailscale_1.10.0_amd64.tgz
RUN wget https://pkgs.tailscale.com/stable/${TSFILE} && \
  tar xzf ${TSFILE} --strip-components=1
COPY . ./

FROM ruby:$ruby_version

RUN mkdir -p /opt/office/app && \
    mkdir -p /opt/office/app/bin
WORKDIR /opt/office/app

COPY --from=tailscale /app/tailscaled /opt/office/app/bin/tailscaled
COPY --from=tailscale /app/tailscale /opt/office/app/bin/tailscale
RUN mkdir -p /var/run/tailscale
RUN mkdir -p /var/cache/tailscale
RUN mkdir -p /var/lib/tailscale

RUN apk add --no-cache build-base ruby-dev sqlite sqlite-dev

COPY $PWD/Gemfile .
COPY $PWD/Gemfile.lock .

RUN bundle install

COPY $PWD .

ENTRYPOINT ["/opt/office/app/bin/entrypoint.sh"]
