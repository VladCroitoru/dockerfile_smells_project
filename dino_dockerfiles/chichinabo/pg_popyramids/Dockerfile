FROM benizar/pg_dw
MAINTAINER Benito Zaragozí <benizar@gmail.com>


################
# Install pg_popyramids
################
WORKDIR /install-ext

ADD doc doc/
ADD sql sql/
ADD test test/
ADD makefile makefile
ADD META.json META.json
ADD pg_popyramids.control pg_popyramids.control

RUN make
RUN make install


WORKDIR /install-ext
ADD init-db.sh /docker-entrypoint-initdb.d/init-db.sh


WORKDIR /
RUN rm -rf /install-ext


