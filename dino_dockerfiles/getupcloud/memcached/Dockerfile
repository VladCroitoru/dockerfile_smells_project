FROM openshift/base-centos7

ENV MEMCACHED_VERSION=1.4 \
    HOME=/

LABEL io.k8s.description="Memcached is a general-purpose distributed memory caching system." \
      io.k8s.display-name="Memcached 1.4" \
      io.openshift.expose-services="11211:memcache" \
      io.openshift.tags="cache,memcached"

RUN yum install --enablerepo=centosplus -y centos-release-scl epel-release && \
    INSTALL_PKGS="libevent-devel libevent" && \
    yum install -y --setopt=tsflags=nodocs --enablerepo=centosplus $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    yum clean all -y

ENV MEMCACHED_VERSION 1.4.25

ENV MEMCACHED_SHA1 7fd0ba9283c61204f196638ecf2e9295688b2314

RUN curl -SL "http://memcached.org/files/memcached-$MEMCACHED_VERSION.tar.gz" -o memcached.tar.gz && \
    echo "$MEMCACHED_SHA1 memcached.tar.gz" | sha1sum -c - && \
    mkdir -p /usr/src/memcached && \
    tar -xzf memcached.tar.gz -C /usr/src/memcached --strip-components=1 && \
    rm memcached.tar.gz && \
    cd /usr/src/memcached && \
    ./configure && \
    make && \
    make install && \
    cd / && rm -rf /usr/src/memcached \

EXPOSE 11211

USER 1001

COPY container-entrypoint /usr/bin/

ENTRYPOINT ["container-entrypoint"]

CMD ["memcached"]
