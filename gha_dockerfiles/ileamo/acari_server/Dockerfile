FROM bitwalker/alpine-elixir-phoenix:1.11.4 AS build
RUN apk --no-cache update && apk --no-cache upgrade && \
    apk --no-cache add openssl autoconf automake libtool nasm zlib-dev

WORKDIR /build

COPY mix.exs .
COPY mix.lock .
#COPY deps deps

ENV MIX_ENV prod

RUN mix deps.get  --only prod

COPY lib lib
#COPY test test
COPY config config
COPY rel rel
COPY src src

# Uncomment line below if you have assets in the priv dir
COPY priv priv
RUN rm -fr priv/static

# Build Phoenix assets
COPY assets assets
RUN cd assets && npm install &&  node node_modules/webpack/bin/webpack.js --mode production
RUN mix phx.digest

RUN rm priv/cert/* && mix phx.gen.cert

RUN mix release bogatka_docker


### Minimal run-time image
FROM alpine:3.14

RUN apk --no-cache update && apk --no-cache upgrade && \
    apk --no-cache add openssl ncurses-libs bash ca-certificates zabbix-utils libstdc++ \
    libcap libcap-dev iproute2 openssh-client su-exec screen iputils busybox-suid bird bird-openrc

RUN adduser -D docker
ARG CWD=/opt/app
WORKDIR ${CWD}

# Copy release from build stage
COPY --from=build /build/_build/prod/rel/bogatka_docker ./

#COPY priv/cert /etc/ssl/acari
#RUN setcap cap_net_admin=ep /opt/app/erts-10.5.2/bin/beam.smp cap_net_admin=ep /sbin/ip

RUN mkdir -p download/uploads
RUN ln -s ${CWD}/download ${CWD}/lib/acari_server-*/priv/static
RUN ln -s ${CWD}/download/uploads /home/docker/uploads

USER docker

# Mutable Runtime Environment
RUN mkdir /tmp/app
ENV RELEASE_MUTABLE_DIR /tmp/app
ENV START_ERL_DATA /tmp/app/start_erl.data

ENV SHELL /bin/bash
COPY docker.bashrc /home/docker/.bashrc

# RUN ssh-keygen -q -t rsa -N '' -f ~/.ssh/id_rsa

USER root

COPY priv/.ssh /home/docker/.ssh
RUN  chown -R docker:docker /home/docker/.ssh
RUN  chmod 0600 /home/docker/.ssh/id_rsa
RUN  chmod 0644 /home/docker/.ssh/id_rsa.pub
RUN  chown -R docker:docker /opt/app

RUN echo "root:docker" | chpasswd

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["start"]
