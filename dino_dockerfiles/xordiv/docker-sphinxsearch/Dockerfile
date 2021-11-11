FROM debian:jessie
MAINTAINER Pavel Laulin <tonebbs@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

ENV SPHINX_VERSION=2.3.2-beta RE2_VERSION=2016-11-01

# install libs, locale and building tools
RUN cd /tmp && apt-get update && \
    apt-get install -y --no-install-recommends make curl ca-certificates libexpat1 libmysqlclient18 libpq5 libodbc1 locales locales libtool re2c \
    autoconf automake libtool g++ libmysqlclient-dev libpq-dev libexpat1-dev && \
    rm -rf /var/lib/apt/lists/* && \
    sed -i 's/# en_US.UTF-8/en_US.UTF-8/' /etc/locale.gen && \
    locale-gen && \
    /usr/sbin/update-locale LANG="en_US.UTF-8" LANGUAGE="en_US:en"


# download and unpack libs and sphinxsearch
RUN cd /tmp && curl -Lo /tmp/snowballstem.tar.gz http://snowball.tartarus.org/dist/libstemmer_c.tgz && \
	tar -xzf  /tmp/snowballstem.tar.gz && \
    curl -Lo /tmp/sphinxsearch.tar.gz http://sphinxsearch.com/files/sphinx-${SPHINX_VERSION}.tar.gz && \
	tar -xzf  /tmp/sphinxsearch.tar.gz  && \
    curl -Lo /tmp/re2.tar.gz https://github.com/google/re2/archive/${RE2_VERSION}.tar.gz && \
	tar -xzf  /tmp/re2.tar.gz

# build sphinxsearch
RUN ls /tmp && cp -R /tmp/libstemmer_c/* /tmp/sphinx-${SPHINX_VERSION}/libstemmer_c/ && \
	sed -i -e 's/stem_ISO_8859_1_hungarian/stem_ISO_8859_2_hungarian/g' /tmp/sphinx-${SPHINX_VERSION}/libstemmer_c/Makefile.in && \
	cp -R /tmp/re2-${RE2_VERSION}/* /tmp/sphinx-${SPHINX_VERSION}/libre2/ && \
	cd /tmp/sphinx-${SPHINX_VERSION} && ./configure --enable-id64 --with-mysql --with-pgsql --with-libstemmer --with-libexpat --with-iconv --with-unixodbc --with-re2 &&\
	make && make install &&\
	rm -rf /tmp/*

# clean image
RUN apt-get remove -y libtool re2c make m4 perl perl-modules autoconf automake g++ gcc && apt-get -y autoremove && apt-get -y autoclean && apt-get -y clean &&  rm -rf /var/lib/apt/lists/* 

# creating dirs
RUN mkdir -p /usr/local/sphinx/data && \
    mkdir -p /var/log/sphinx && \
    mkdir -p /usr/local/sphinx/rlp && \
    mkdir -p /usr/local/sphinx/lib && \
    mkdir -p /usr/local/sphinx/dicts && \
    mkdir -p /usr/local/sphinx/plugins && \
    mkdir -p /usr/local/sphinx/etc/conf.d

# add custom dicts
ADD dicts /usr/local/sphinx/dicts


VOLUME ["/usr/local/sphinx/data", "/var/log/sphinx", "/usr/local/sphinx/etc/conf.d"]

# 9312 Sphinx
# 9306 SphinxQL
EXPOSE 9312 9306

COPY /scripts/* /
COPY /conf/* /usr/local/sphinx/etc/

ENTRYPOINT ["/docker-entry.sh"]
CMD ["/docker-cmd.sh"]
