FROM postgres:10
RUN apt-get update && apt-get install --no-install-recommends -y mysql-client wget unzip make gcc postgresql-server-dev-10 libmysql++-dev ca-certificates \
    libhiredis-dev && \
    wget https://github.com/EnterpriseDB/mysql_fdw/archive/master.zip -O /opt/mysql_fdw.zip && \
    wget https://github.com/pg-redis-fdw/redis_fdw/archive/REL_10_STABLE.zip -O /opt/redis_fdw.zip && \
    cd /opt && unzip mysql_fdw && \
    cd /opt/mysql_fdw-master && make USE_PGXS=1 && make install USE_PGXS=1 && \
    cd /opt && unzip redis_fdw && \
    cd /opt/redis_fdw-REL_10_STABLE && make USE_PGXS=1 && make install USE_PGXS=1 && \
    apt-get remove -y wget unzip make gcc postgresql-server-dev-10 libmysql++-dev && \
    rm -rf /var/lib/apt/lists/*

