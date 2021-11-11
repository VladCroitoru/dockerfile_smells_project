FROM benizar/postgres-ext:9.6

# Basic build-time metadata as defined at http://label-schema.org
LABEL org.label-schema.name="pg_adm" \
      org.label-schema.description="Docker container for developing and testing the pg_adm extension." \
      org.label-schema.version="9.6" \
      org.label-schema.vcs-url="https://github.com/benizar/pg_adm" \
      org.label-schema.vendor="benito-zaragozi.com" \
      org.label-schema.schema-version="1.0"

########################
# Versions and sources #
########################
#from https://github.com/benizar/
#ENV SOURCE https://github.com/benizar/
ENV SAKILA https://github.com/benizar/pg_sakila_db.git

########################
# Install pg_sakila_db #
########################
WORKDIR /install-ext
RUN git clone $SAKILA
WORKDIR /install-ext/pg_sakila_db
RUN make
RUN make install

##################
# Install pg_adm #
##################
WORKDIR /install-ext

ADD doc doc/
ADD sql sql/
ADD test test/
ADD makefile makefile
ADD META.json META.json
ADD pg_adm.control pg_adm.control

RUN make
RUN make install


WORKDIR /
RUN rm -rf /install-ext

ADD init-db.sh /docker-entrypoint-initdb.d/init-db.sh


