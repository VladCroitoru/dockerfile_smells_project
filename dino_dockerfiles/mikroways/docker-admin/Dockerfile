FROM krlmlr/debian-ssh

MAINTAINER Leandro Di Tommaso <leandro.ditommaso@mikroways.net>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update                              && \
    apt-get install --no-install-recommends -qy    \
                    mysql-client                   \
                    postgresql-client              \
                    rsync                          \
                    vim                         && \
    apt-get clean                               && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 
