FROM eeacms/centos:7s
MAINTAINER "Olimpiu Rob" <olimpiu.rob@eaudeweb.ro>

ENV EGGSHOP http://eggshop.eaudeweb.ro
ENV POUND_VERSION Pound-2.7
ENV POUND_CUSTOM _fix_cookie
ENV POUND_SRC $POUND_VERSION$POUND_CUSTOM.tgz
ENV POUND_URL_PATH $EGGSHOP/$POUND_SRC
ENV POUND_USER pound
ENV POUND_GROUP pound
ENV POUND_HOME /opt/pound
ENV INOTIFY_SRC http://github.com/downloads/rvoicilas/inotify-tools/inotify-tools-3.14.tar.gz

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "/tmp/get-pip.py" && \
    python /tmp/get-pip.py && \
    pip install j2cli && \
    python3.4 /tmp/get-pip.py && \
    pip3 install chaperone

RUN mkdir -p $POUND_HOME/install && \
    groupadd -g 500 -f -r $POUND_GROUP && \
    useradd -u 500 -r -g $POUND_GROUP -d $POUND_HOME -s /sbin/nologin \
    -c "Pound user" $POUND_USER

RUN mkdir -p /tmp/pound/install && \
    curl -SL $POUND_URL_PATH | \
    tar -xzC /tmp/pound/install && \
    cd /tmp/pound/install/$POUND_VERSION && \
    ./configure --with-owner=$POUND_USER --with-group=$POUND_GROUP \
    --prefix=/opt/pound && \
    make -C /tmp/pound/install/$POUND_VERSION && \
    make -C /tmp/pound/install/$POUND_VERSION install


RUN cd /tmp && \
    curl -L $INOTIFY_SRC -o "/tmp/inotify.tar.gz" && \
    tar -zxvf /tmp/inotify.tar.gz && \
    cd /tmp/inotify-tools-3.14/ && \
    ./configure && \
    make && make install

COPY src/chaperone.conf            /etc/chaperone.d/chaperone.conf

COPY src/docker-setup.sh           /opt/docker-setup.sh
COPY src/reload.sh                 /opt/reload.sh

COPY src/configure.py              /opt/configure.py
COPY src/track-hosts.sh            /opt/track_hosts.sh
COPY src/backends.j2               /opt/pound/etc/backends.j2

RUN mkdir -p $POUND_HOME/var && \
    chown -R $POUND_USER:$POUND_GROUP $POUND_HOME

USER $POUND_USER

ENTRYPOINT ["/usr/bin/chaperone", "--user=pound"]
