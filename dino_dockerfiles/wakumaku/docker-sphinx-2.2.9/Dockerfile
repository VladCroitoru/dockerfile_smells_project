FROM debian:8.7

RUN apt-get update

RUN apt-get install -y \
    wget \
    tar \
    build-essential \
    unixodbc-dev \
    expat \
    libmysqlclient-dev

COPY install/*.tar.gz /opt/install/

WORKDIR /opt/install

RUN cat *.tar.gz | tar -xvzf - -i && \
    cp -R libstemmer_c/* sphinx-2.2.9-release/libstemmer_c/ && \
    cp -R re2-2015-05-01/* sphinx-2.2.9-release/libre2/

RUN cd sphinx-2.2.9-release && \
    ./configure --with-libstemmer --with-libexpat --with-iconv --with-unixodbc --with-re2 && \
    make && \
    make install

WORKDIR /

RUN mkdir -p /var/idx/sphinxsearch && \
    mkdir -p /var/log/sphinxsearch && \
    mkdir -p /var/lib/sphinxsearch && \
    mkdir -p /var/run/sphinxsearch

VOLUME ["/var/idx/sphinxsearch", "/var/log/sphinxsearch", "/var/lib/sphinxsearch", "/var/run/sphinxsearch"]

COPY ./scripts /opt/scripts
RUN chmod +x /opt/scripts/*.sh

RUN apt-get remove -y \
    build-essential && \
    apt-get autoremove -y && \
    rm -rf /opt/install

EXPOSE 9312 9306

CMD ["/opt/scripts/indexall.sh"]
