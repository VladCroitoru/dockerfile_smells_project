FROM erikadp/ubuntu-trusty-java8

ENV ANT_VERSION 1.9.6
RUN apt-get update \
    && apt-get install -y wget \
    && cd  \
    && wget -q http://archive.apache.org/dist/ant/binaries/apache-ant-${ANT_VERSION}-bin.tar.gz  \
    && tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz  \
    && mv apache-ant-${ANT_VERSION} /opt/ant  \
    && rm apache-ant-${ANT_VERSION}-bin.tar.gz
ENV ANT_HOME /opt/ant
ENV PATH ${PATH}:/opt/ant/bin