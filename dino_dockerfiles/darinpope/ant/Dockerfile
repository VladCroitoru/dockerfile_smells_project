FROM java:7u95-jdk

MAINTAINER darinpope <darin@planetpope.com>

ENV ANT_VERSION=1.9.2
ENV ANT_HOME=/opt/ant

ENV MVN_VERSION=3.2.1

# change to tmp folder
WORKDIR /tmp

# Download and extract apache ant to opt folder
RUN wget --no-check-certificate --no-cookies http://archive.apache.org/dist/ant/binaries/apache-ant-${ANT_VERSION}-bin.tar.gz \
    && wget --no-check-certificate --no-cookies http://archive.apache.org/dist/ant/binaries/apache-ant-${ANT_VERSION}-bin.tar.gz.md5 \
    && echo "$(cat apache-ant-${ANT_VERSION}-bin.tar.gz.md5) apache-ant-${ANT_VERSION}-bin.tar.gz" | md5sum -c \
    && tar -zvxf apache-ant-${ANT_VERSION}-bin.tar.gz -C /opt/ \
    && ln -s /opt/apache-ant-${ANT_VERSION} /opt/ant \
    && rm -f apache-ant-${ANT_VERSION}-bin.tar.gz \
    && rm -f apache-ant-${ANT_VERSION}-bin.tar.gz.md5

# add executables to path
RUN update-alternatives --install "/usr/bin/ant" "ant" "/opt/ant/bin/ant" 1 && \
    update-alternatives --set "ant" "/opt/ant/bin/ant" 
    
RUN wget --no-check-certificate --no-cookies https://archive.apache.org/dist/maven/maven-3/${MVN_VERSION}/binaries/apache-maven-${MVN_VERSION}-bin.tar.gz \
    && wget --no-check-certificate --no-cookies https://archive.apache.org/dist/maven/maven-3/${MVN_VERSION}/binaries/apache-maven-${MVN_VERSION}-bin.tar.gz.md5 \
    && echo "$(cat apache-maven-${MVN_VERSION}-bin.tar.gz.md5) apache-maven-${MVN_VERSION}-bin.tar.gz" | md5sum -c \
    && tar -zvxf apache-maven-${MVN_VERSION}-bin.tar.gz -C /opt/ \
    && ln -s /opt/apache-maven-${MVN_VERSION} /opt/maven \
    && rm -f apache-maven-${MVN_VERSION}-bin.tar.gz \
    && rm -f apache-maven-${MVN_VERSION}-bin.tar.gz.md5

RUN update-alternatives --install "/usr/bin/mvn" "mvn" "/opt/maven/bin/mvn" 1 && \
    update-alternatives --set "mvn" "/opt/maven/bin/mvn" 

# change to root folder
WORKDIR /root
