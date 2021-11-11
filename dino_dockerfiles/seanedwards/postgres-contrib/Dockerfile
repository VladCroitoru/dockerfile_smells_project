FROM postgres

RUN apt-get update
RUN apt-get -y install protobuf-c-compiler libprotobuf-c0-dev unzip git

WORKDIR /usr/src/postgres/contrib

RUN make -j"$(nproc)"
RUN make install

WORKDIR /usr/src
RUN git clone https://github.com/citusdata/cstore_fdw.git
WORKDIR /usr/src/cstore_fdw

RUN make -j"$(nproc)"
RUN make install

WORKDIR /usr/src/postgres

VOLUME /var/lib/postgresql/data
ENTRYPOINT ["/usr/src/postgres/docker-entrypoint.sh"]
EXPOSE 5432
CMD ["postgres"]



