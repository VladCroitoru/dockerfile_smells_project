FROM mysql:5.7

RUN apt-get update && \
    apt-get install -y --no-install-recommends --no-install-suggests \
    vim netcat-openbsd

ADD https://github.com/github/gh-ost/releases/download/v1.0.48/gh-ost-binary-linux-20190214020851.tar.gz /tmp/gh-ost.tar.gz
RUN mkdir -p /tmp/gh-ost && \
    tar zxvf /tmp/gh-ost.tar.gz -C /tmp/gh-ost && \
    mv /tmp/gh-ost/gh-ost /usr/local/bin/

ADD https://github.com/ichirin2501/mysql_random_data_load/releases/download/patch-01/mysql_random_data_load_patch_01_linux_amd64.tar.gz /tmp/mysql_random_data_load.tar.gz
RUN mkdir -p /tmp/mysql_random_data_load && \
    tar zxvf /tmp/mysql_random_data_load.tar.gz -C /tmp/mysql_random_data_load && \
    mv /tmp/mysql_random_data_load/mysql_random_data_load /usr/local/bin

HEALTHCHECK --interval=5s --timeout=3s CMD test -e /tmp/OK
