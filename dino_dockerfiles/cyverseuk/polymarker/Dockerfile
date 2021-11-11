FROM ubuntu:14.04

LABEL ruby.version="2.2" exonerate.version="2.2.0" glib.version="2.31.12" mafft.version="7.123b" primer3.version="2.3.6"

ARG DEBIAN_FRONTEND=noninteractive

USER root

RUN     apt-get -y update && apt-get -yy install apt-utils make g++ libreadline6 libreadline6-dev libssl-dev libreadline-dev curl git-core python-software-properties build-essential zlib1g-dev libyaml-dev libgdbm-dev libncurses5-dev libpq-dev libffi-dev xorg openbox openssl zlib1g-dev autoconf  automake libtool bison sqlite patch bzip2 bison gcc wget ruby-full ruby-dev libgmpxx4ldbl gawk-doc libgmp10-doc libmpfr-dev sqlite3-doc gawk libsqlite3-dev pkg-config mafft exonerate primer3 && \
        gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 && \
        \curl -sSL https://get.rvm.io | bash -s stable && \
        echo source /etc/profile.d/rvm.sh >> /.bashrc && \
        /bin/bash -c "source /.bashrc; rvm install 2.2; rvm use 2.2 --default;gem install bio-polyploid-tools"
      
WORKDIR /data/

