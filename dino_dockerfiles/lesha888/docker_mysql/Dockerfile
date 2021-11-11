FROM percona:5.6

RUN  apt-get update && apt-get install -y libjemalloc-dev libhiredis-dev libapr1-dev libaprutil1-dev  gcc make   libmysqlclient-dev unzip
ADD https://github.com/lesha888/mysql2redis/archive/master.zip /usr/local/src/

RUN ln -s /usr/include/apr-1.0 /usr/include/apr-1 && \
cd /usr/local/src/ && \
unzip -qq master.zip && \
cd /usr/local/src/mysql2redis-master && \
make && \
make install && \
cd /usr/local/src/ && \
rm -r /usr/local/src/mysql2redis-master

#COPY conf.d /etc/mysql/conf.d
#RUN	echo '!includedir /etc/mysql/conf.d/' > /etc/mysql/my.cnf
RUN mkdir /tmp/mysqltmp && \
chmod 777 /tmp/mysqltmp && \
chown -R mysql:mysql /etc/mysql/conf.d 


