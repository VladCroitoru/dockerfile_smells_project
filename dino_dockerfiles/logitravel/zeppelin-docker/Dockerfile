FROM logitravel/spark-docker:2.1.0

LABEL MAINTAINER Cristòfol Torrens Morell "piffall@gmail.com"

# Install Zeppelin
ENV ZEPPELIN_VERSION 0.7.2
ENV ZEPPELIN_HOME /usr/zeppelin-${ZEPPELIN_VERSION}
RUN \
    mkdir ${ZEPPELIN_HOME} && \
    wget http://apache.uvigo.es/zeppelin/zeppelin-${ZEPPELIN_VERSION}/zeppelin-${ZEPPELIN_VERSION}-bin-all.tgz && \
    tar vxzf zeppelin-${ZEPPELIN_VERSION}-bin-all.tgz --strip 1 -C ${ZEPPELIN_HOME} && \
    rm zeppelin-${ZEPPELIN_VERSION}-bin-all.tgz

# Add zeppelin bin path to PATH
ENV PATH $PATH:${ZEPPELIN_HOME}/bin
