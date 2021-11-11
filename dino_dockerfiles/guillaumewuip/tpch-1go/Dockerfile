# Dockerfile
FROM wnameless/oracle-xe-11g


RUN apt-get update -y
RUN apt-get install -y git make gcc

RUN git clone https://github.com/electrum/tpch-dbgen

RUN cd tpch-dbgen; make
RUN cd tpch-dbgen; ./dbgen -s 1 -f

ADD create_table.sql /docker-entrypoint-initdb.d/
ADD generate_data.sh /docker-entrypoint-initdb.d/

ADD *.ctl /load_files/
