FROM google/golang

RUN cd /usr/local/src && git clone http://github.com/coreos/rudder.git && \
    cd /usr/local/src/rudder && ./build

ADD ./busybox-rudder/Dockerfile /usr/local/src/rudder/Dockerfile

CMD docker build --rm --force-rm -t gurpartap/rudder /usr/local/src/rudder/
