FROM postgres:9

RUN set -eux; \
	apt-get update && apt-get install -y --no-install-recommends \
		g++ \
		gcc \
		libc6-dev \
		make \
		p7zip-full \
		curl \
		ca-certificates \
		git \
		pkg-config \
        default-jdk \
        python \
        python3-dev \
		python3-pip \
        python3-setuptools; \
    pip3 install --no-cache-dir \
        nltk \
        cython; \
	apt-get clean; \
	rm -rf /var/lib/apt/lists/*;

#install latest petsc
ENV PETSC_DOWNLOAD_URL https://ftp.mcs.anl.gov/pub/petsc/petsc-lite-3.9.tar.gz
ENV PETSC_ARCH arch-linux2-c-opt
ENV PETSC_DIR /usr/local/petsc
ENV PETSC_LIB $PETSC_DIR/$PETSC_ARCH/lib/
ENV LD_LIBRARY_PATH $PETSC_LIB:$LD_LIBRARY_PATH
RUN set -eux; \
    cd $PETSC_DIR/..; \
    curl -fsSL "$PETSC_DOWNLOAD_URL" -o petsc.tar.gz; \
    tar -xzf petsc.tar.gz; \
    rm petsc.tar.gz; \
    mv petsc* petsc; \
    cd $PETSC_DIR; \
    ./configure --with-cc=gcc --with-cxx=0 --with-fc=0 --with-debugging=0 \
#        Optimization: if compiled somewhere, may not work elsewhere.
#        COPTFLAGS='-O3 -march=native -mtune=native' \
        --download-mpich --download-f2cblaslapack; \
    make all test; \
    rm -rf /tmp/* /var/tmp/*;

#install latest golang
ENV GO_DIR /usr/local/go
ENV GOPATH /go
ENV PATH $GOPATH/bin:$GO_DIR/bin:$PATH
RUN set -eux; \
	cd $GO_DIR/..; \
    V=10; \
    while curl --output /dev/null --silent --head --fail "https://dl.google.com/go/go1.$V.linux-amd64.tar.gz"; do \
        GO_DOWNLOAD_URL="https://dl.google.com/go/go1.$V.linux-amd64.tar.gz"; \
        V=$((V+1)); \
    done; \
    V=$((V-1)); \
    v=1; \
    while curl --output /dev/null --silent --head --fail "https://dl.google.com/go/go1.$V.$v.linux-amd64.tar.gz"; do \
        GO_DOWNLOAD_URL="https://dl.google.com/go/go1.$V.$v.linux-amd64.tar.gz"; \
        v=$((v+1)); \
    done; \
    curl -fsSL "$GO_DOWNLOAD_URL" -o go.tar.gz; \
	tar -xzf go.tar.gz; \
	rm go.tar.gz; \
	mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"; \
	go version;

#install and compile the project
ENV PROJECT github.com/negapedia/negapedia
ADD . $GOPATH/src/$PROJECT
RUN set -eux; \
cd /; \
echo "#!/usr/bin/env bash\n\
set -e;\n\
\n\
#Fork exec the postgres docker-entrypoint with postgres as command \n\
postgres-entrypoint() {\n\
set -- postgres\n\
$(cat docker-entrypoint.sh)\n\
}; postgres-entrypoint > /dev/null 2>&1 &\n\
\n\
mkdir -p /data/csv;\n\
chown -R \$(stat -c '%u:%g' /data) /data;\n\
\n\
echo CREATING CLUSTER;\n\
pg_createcluster 9.6 main; \n\
echo STARTING PSQL;\n\
/etc/init.d/postgresql start;\n\
echo SETTING UP FILES;\n\
echo "local   all             postgres                                trust" >> /etc/postgresql/9.6/main/pg_hba.conf\n\
#echo "listen_addresses='*'" >> /etc/postgresql/9.6/main/postgresql.conf\n\
# /usr/lib/postgresql/9.6/bin/postgres -D /var/lib/postgresql/9.6/main -c  config_file=/etc/postgresql/9.6/main/postgresql.conf\n\
echo RESTARTING THE SERVER;\n\
/etc/init.d/postgresql restart;\n\
apt-get update && apt-get install sudo;\n\
echo CHANGING PWD POSTGRES\n\
sudo -u postgres psql -c \"ALTER USER postgres PASSWORD 'postgres';\"\n\
#/usr/lib/postgresql/9.6/bin/pg_ctl -D /var/lib/postgresql/9.6/main -l logfile start\n\
\n\
exec \"\$@\"\n\n \"" > docker-entrypoint.sh; \

go get $PROJECT/...;
RUN git clone https://github.com/negapedia/wikitfidf.git /go/src/github.com/negapedia/wikitfidf;

WORKDIR /data
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["refresh"]
