FROM golang:1.8.3
WORKDIR /go/src/github.com/wadahiro/mod_auth_openidc-test/
COPY *.go .
RUN go get github.com/dgrijalva/jwt-go 
RUN go get github.com/pkg/errors
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo oidc_dummy_server.go

FROM centos:7.3.1611
LABEL maintainer "wadahiro@gmail.com"

ENV HTTPD_VERSION=2.4.6-45.el7.centos \
    MOD_AUTH_OPENIDC_VERSION=2.3.1-1.el7.centos.x86_64 \
    MOD_AUTH_OPENIDC_SHORT_VERSION=2.3.1 \
    HIREDIS_VERSION=0.12.1-1.el7.x86_64 \
    CJOSE_VERSION=0.5.1-1.el7.centos.x86_64

## Fix centos version
RUN \
  echo 7.3.1611 > /etc/yum/vars/releasever \
  && sed -i -e "s/^mirrorlist=/#mirrorlist=/g" /etc/yum.repos.d/CentOS-Base.repo \
  && sed -i -e "s/^#baseurl=/baseurl=/g" /etc/yum.repos.d/CentOS-Base.repo \
  && sed -i -e "s/^mirrorlist=/#mirrorlist=/g" /etc/yum.repos.d/CentOS-fasttrack.repo \
  && sed -i -e "s/^#baseurl=/baseurl=/g" /etc/yum.repos.d/CentOS-fasttrack.repo


## Install debug modules
RUN set -x \
  && yum install -y gcc make bzip2 perl

WORKDIR /build/
RUN \
    curl -L http://sourceware.org/pub/valgrind/valgrind-3.13.0.tar.bz2 > valgrind.tar.bz2 \
    && tar xvfj valgrind.tar.bz2 \
    && cd valgrind-* \
    && ./configure \
    && make \
    && make install

RUN yum install -y pcre-devel expat-devel file

RUN \
    curl -L http://ftp.tsukuba.wide.ad.jp/software/apache//httpd/httpd-2.4.27.tar.gz > httpd.tar.gz \
    && curl -L http://ftp.meisei-u.ac.jp/mirror/apache/dist//apr/apr-1.6.2.tar.gz > apr.tar.gz \
    && curl -L http://ftp.meisei-u.ac.jp/mirror/apache/dist//apr/apr-util-1.6.0.tar.gz > apr-util.tar.gz \
    && tar xvzf httpd.tar.gz \
    && tar xvzf apr.tar.gz \
    && tar xvzf apr-util.tar.gz \
    && rm -f httpd.tar.gz \
    && rm -f apr.tar.gz \
    && rm -f apr-util.tar.gz \
    && mv apr-util-* httpd-2.4.27/srclib/apr-util \
    && mv apr-* httpd-2.4.27/srclib/apr \
    && cd httpd-* \
    && CFLAGS="-g" ./configure --enable-mpms-shared=all --with-included-apr --enable-threads \
    && make \
    && make install


RUN yum install -y epel-release
RUN yum install -y libhiredis-devel jansson-devel libcurl-devel openssl-devel autoconf automake

RUN \
  curl -L https://github.com/pingidentity/mod_auth_openidc/releases/download/v2.3.0/cjose-0.5.1.tar.gz > cjose.tar.gz \
  && tar xvzf cjose.tar.gz \
  && rm -f cjose.tar.gz \
  && cd cjose-* \
  && ./configure CFLAG="-g" \
  && make \
  && make install

RUN \
  curl -L https://github.com/pingidentity/mod_auth_openidc/releases/download/v2.3.1/mod_auth_openidc-2.3.1.tar.gz > mod_auth_openidc.tar.gz \
  && tar xvzf mod_auth_openidc.tar.gz \
  && rm -f mod_auth_openidc.tar.gz \
  && export PKG_CONFIG_PATH=/usr/local/apache2/lib/pkgconfig:/usr/local/lib/pkgconfig \
  && cd mod_auth_openidc-* \
  && ./autogen.sh \
  && ./configure --with-apxs2=/usr/local/apache2/bin/apxs \
  && make \
  && make install


## Install distributed modules
RUN \
  yum install -y httpd-${HTTPD_VERSION}

RUN \
  cd /tmp \
  && curl -L -O https://dl.fedoraproject.org/pub/epel/7/x86_64/h/hiredis-${HIREDIS_VERSION}.rpm \
  && curl -L -O https://github.com/pingidentity/mod_auth_openidc/releases/download/v2.3.0/cjose-${CJOSE_VERSION}.rpm \
  && curl -L -O https://github.com/pingidentity/mod_auth_openidc/releases/download/v${MOD_AUTH_OPENIDC_SHORT_VERSION}/mod_auth_openidc-${MOD_AUTH_OPENIDC_VERSION}.rpm \
  && yum install -y *.rpm \
  && rm -rf /tmp/*.rpm


## Install dummmy oidc server & apps
COPY --from=0 /go/src/github.com/wadahiro/mod_auth_openidc-test/oidc_dummy_server /usr/local/bin/
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/*

## Configure httpd
RUN \
  ln -sf /dev/stdout /usr/local/apache2/logs/access_log \
  && ln -sf /dev/stderr /usr/local/apache2/logs/error_log \
  && ln -sf /dev/stdout /var/log/httpd/access_log \
  && ln -sf /dev/stderr /var/log/httpd/error_log \
  && ln -sf /dev/stdout /var/log/valgrind.log

RUN echo "Include conf.d/*.conf" >> /usr/local/apache2/conf/httpd.conf

COPY server.conf /usr/local/apache2/conf.d/
COPY server.conf /etc/httpd/conf.d/

RUN sed -i -e "s/^LoadModule mpm_event_module/#LoadModule mpm_event_module/" /usr/local/apache2/conf/httpd.conf
COPY 00-mpm.conf /usr/local/apache2/conf.d/
COPY 00-mpm.conf /etc/httpd/conf.modules.d/

EXPOSE 80
EXPOSE 8080

CMD [ "/usr/local/bin/docker-entrypoint.sh" ]

