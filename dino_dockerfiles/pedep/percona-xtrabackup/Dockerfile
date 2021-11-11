FROM percona:5.7.16

RUN apt-get update && yes N | apt-get install -y \
  --no-install-suggests percona-xtrabackup-24 \
  && rm -rf /var/lib/apt/lists/*
