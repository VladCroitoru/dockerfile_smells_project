FROM ubuntu:14.04

MAINTAINER ivlis

COPY scripts/* /root/

WORKDIR /root

ENV ERLANG_VER OTP-18.0.3
ENV REBAR_VER 2.6.0

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/erlang/bin/

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    build-essential gawk m4 libcurl3 xdg-utils autoconf \
    git-core ca-certificates wget openssh-client\
    libncurses-dev libssl-dev && \
    tar -zxvf erln8_ubuntu1404.tgz && \
    /bin/bash /root/install-erln8.sh && \
    erln8/erln8 --build ${ERLANG_VER} --config=min &&\
    mkdir -p /opt/erlang/ && \
    cp -a /root/.erln8.d/otps/${ERLANG_VER}/dist/bin /opt/erlang/ && \
    cp -a /root/.erln8.d/otps/${ERLANG_VER}/dist/lib /opt/erlang/ && \
    sed -e "s|/root/.erln8.d/otps/${ERLANG_VER}/dist|/opt/erlang|g" -i /opt/erlang/bin/erl && \
    sed -e "s|/root/.erln8.d/otps/${ERLANG_VER}/dist|/opt/erlang|g" -i /opt/erlang/lib/erlang/bin/erl && \
    sed -e "s|/root/.erln8.d/otps/${ERLANG_VER}/dist|/opt/erlang|g" -i /opt/erlang/lib/erlang/bin/start && \
    sed -e "s|/root/.erln8.d/otps/${ERLANG_VER}/dist|/opt/erlang|g" -i /opt/erlang/lib/erlang/releases/RELEASES && \
    sed -e "s|/root/.erln8.d/otps/${ERLANG_VER}/dist|/opt/erlang|g" -i /opt/erlang/lib/erlang/erts-*/bin/erl && \
    sed -e "s|/root/.erln8.d/otps/${ERLANG_VER}/dist|/opt/erlang|g" -i /opt/erlang/lib/erlang/erts-*/bin/start && \
    erln8/reo --build ${REBAR_VER} && \
    mv  /root/.erln8.d/rebars/${REBAR_VER}/rebar  /opt/erlang/bin/ && \
    rm -rf /root/.erln8.d && \
    rm -rf /root/erln8/ && \
    rm -rf /tmp/* && \
    apt-get purge -y \
    build-essential gawk m4 autoconf \
    git-core ca-certificates wget \
    libncurses-dev libssl-dev && \
    apt-get autoremove -y && \
    apt-get clean


