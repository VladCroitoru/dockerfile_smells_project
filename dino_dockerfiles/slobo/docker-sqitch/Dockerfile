FROM perl:5.22.4

RUN \
  apt-get update \
  && apt-get install -y \
    libdbd-pg-perl postgresql-client libpq-dev \
    mysql-client \
    zsh \
    pv

RUN \
  cpanm -v -n DBD::Pg DBD::mysql Template DWHEELER/App-Sqitch-0.9997.tar.gz \
  && rm -rf /root/.cpanm

