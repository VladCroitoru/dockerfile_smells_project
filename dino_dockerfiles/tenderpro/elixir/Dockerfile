FROM debian:jessie

MAINTAINER Alexey Kovrizhkin <lekovr+tpro@gmail.com>

ENV DOCKERFILE_VERSION  180425

ENV DEBIAN_FRONTEND noninteractive
ENV INITRD No

ENV GOSU_VER=1.10

# user op
RUN useradd -m -r -s /bin/bash -Gwww-data -gusers -gsudo op

# -------------------------------------------------------------------------------
# Run custom setup scripts

RUN apt-get update && apt-get install -y \
     libwxbase3.0-0 libwxgtk3.0-0 libsctp1 wget git locales curl make python \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV LANG en_US.utf8

RUN arch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
  && curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/${GOSU_VER}/gosu-$arch" \
  && chmod +x /usr/local/bin/gosu \
  && wget -nv https://packages.erlang-solutions.com/erlang/esl-erlang/FLAVOUR_1_general/esl-erlang_20.3-1~debian~jessie_${arch}.deb \
  && dpkg -i esl-erlang_20.3-1~debian~jessie_${arch}.deb \
  && rm esl-erlang_20.3-1~debian~jessie_${arch}.deb \
  && wget -nv https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb \
  && dpkg -i erlang-solutions_1.0_all.deb \
  && rm erlang-solutions_1.0_all.deb \
  && apt-get update \
  && apt-get install elixir \
  && rm -rf /var/lib/apt/lists/*

# -------------------------------------------------------------------------------
# Get local deps

COPY mix.exs /root/mix.exs
RUN cd /root \
  && mix do local.hex --force, local.rebar --force, deps.get

# ------------------------------------------------------------

WORKDIR /home/app

ENV APPUSER op
