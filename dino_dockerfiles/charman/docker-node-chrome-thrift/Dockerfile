FROM charman/docker-node-chrome:latest

# Install Thrift 0.10.0
WORKDIR /opt/thrift
RUN wget http://mirror.cc.columbia.edu/pub/software/apache/thrift/0.10.0/thrift-0.10.0.tar.gz && \
    tar xvfz thrift-0.10.0.tar.gz
WORKDIR /opt/thrift/thrift-0.10.0
RUN ./configure --with-nodejs --without-c_glib --without-python && \
    make && \
    make install
