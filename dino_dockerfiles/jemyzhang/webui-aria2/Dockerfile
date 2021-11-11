FROM ubuntu

# less priviledge user, the id should map the user the downloaded files belongs to
RUN groupadd -r dummy && useradd -r -g dummy dummy -u 1000

# webui + aria2
RUN apt-get update \
    && apt-get install -y busybox curl \
    git \
    make g++ libssl-dev nettle-dev libgmp-dev libssh2-1-dev libc-ares-dev libxml2-dev zlib1g-dev libsqlite3-dev pkg-config libxml2-dev libcppunit-dev autoconf automake autotools-dev autopoint libtool \
    && ARIA2_VERSION="1.30.0" \
    && mkdir aria_build && cd aria_build \
    && curl -L https://github.com/aria2/aria2/releases/download/release-"$ARIA2_VERSION"/aria2-"$ARIA2_VERSION".tar.gz > aria2.tar.gz \
    && tar -xzf aria2.tar.gz \
    && cd aria2-$ARIA2_VERSION \
    && autoreconf -i  && ./configure && make \
    && mv src/aria2c /usr/bin/ \
    && cd ../.. \
    && rm -rf aria_build \
    && apt-get remove -y --purge --auto-remove make g++ libssl-dev nettle-dev libgmp-dev libssh2-1-dev libc-ares-dev libxml2-dev zlib1g-dev libsqlite3-dev pkg-config libxml2-dev libcppunit-dev autoconf automake autotools-dev autopoint libtool \
    && apt-get install -y libxml2 libsqlite3-0 libc-ares2 zlib1g libssh2-1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ADD . /webui-aria2

# gosu install latest
RUN GITHUB_REPO="https://github.com/tianon/gosu" \
  && LATEST=`curl -s  $GITHUB_REPO"/releases/latest" | grep -Eo "[0-9].[0-9]*"` \
  && curl -L $GITHUB_REPO"/releases/download/"$LATEST"/gosu-amd64" > /usr/local/bin/gosu \
  && chmod +x /usr/local/bin/gosu

# goreman supervisor install latest
RUN GITHUB_REPO="https://github.com/mattn/goreman" \
  && LATEST=`curl -s  $GITHUB_REPO"/releases/latest" | grep -Eo "v[0-9]*.[0-9]*.[0-9]*"` \
  && curl -L $GITHUB_REPO"/releases/download/"$LATEST"/goreman_linux_amd64.tar.gz" > goreman.tar.gz \
  && tar -xvzf goreman.tar.gz && mv /goreman_linux_amd64/goreman /usr/local/bin/goreman && rm -R goreman*

# goreman setup
RUN echo "web: gosu dummy /bin/busybox httpd -f -p 8080 -h /webui-aria2\nbackend: gosu dummy /usr/bin/aria2c --enable-rpc --rpc-listen-all --dir=/data" > Procfile

# aria2 downloads directory
VOLUME /data

# aria2 RPC port, map as-is or reconfigure webui
EXPOSE 6800/tcp

# webui static content web server, map wherever is convenient
EXPOSE 8080/tcp

CMD ["start"]
ENTRYPOINT ["/usr/local/bin/goreman"]
