# --- INSTALL SCALA --- 
# https://github.com/broadinstitute/scala-baseimage/blob/31aad6024d7fbe7e8f54ee2ab190a39aad6c9156/Dockerfile
#
# This base image is meant for Scala applications
# And specifically scala web services.  It is build
# using a baseimage that installs runit to launch
# and monitor services.

# http://phusion.github.io/baseimage-docker/
FROM phusion/baseimage:0.9.17

ENV TERM=xterm-256color \
    SCALA_VERSION=2.11.7 \
    SBT_VERSION=0.13.9 \
    JAVA_VERSION=8 \
    JAVA_HOME=/usr/lib/jvm/java-8-oracle/jre

# Use baseimage's init system.
CMD ["/sbin/my_init"]

RUN apt-get update && apt-get install -y wget tree htop zip unzip && \
    add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) multiverse" && \
    add-apt-repository -y ppa:webupd8team/java && \
    echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-set-selections && \
    echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-selections && \
    apt-get update && \
    apt-get install -y oracle-java${JAVA_VERSION}-installer && \
    # Install Java Cryptography Extensions to allow Java programs to use longer bit-length encryption (e.g. AES-256)
    # See: http://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html
    curl -LO "http://download.oracle.com/otn-pub/java/jce/8/jce_policy-8.zip" -H 'Cookie: oraclelicense=accept-securebackup-cookie' && \
    unzip jce_policy-8.zip && \
    cp UnlimitedJCEPolicyJDK8/*.jar $JAVA_HOME/lib/security && \
    rm -rf jce_policy-8.zip UnlimitedJCEPolicyJDK8 && \
    # Download and install Scala, SBT
    wget http://www.scala-lang.org/files/archive/scala-${SCALA_VERSION}.deb && \
    wget http://dl.bintray.com/sbt/debian/sbt-${SBT_VERSION}.deb && \
    dpkg -i scala-${SCALA_VERSION}.deb && \
    dpkg -i sbt-${SBT_VERSION}.deb && \
    apt-get update && \
    apt-get install -y scala sbt && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /*.deb && \
    # This next command makes SBT download all JARs necessary to run so using SBT the first time isn't so painful.
    echo "exit" | sbt

# --- INSTALL REACH ---
# https://github.com/clulab/reach/tree/72064c6abb442bfa84cc89e0f00fb50c3a9ffa6c

RUN apt-get update && apt-get install -y git

# Fetch the branch and checkout commit 
RUN mkdir -p /nlp

# Fetch the branch and checkout commit 
RUN cd /nlp && git clone -b master https://github.com/clulab/reach.git
WORKDIR /nlp/reach
RUN git checkout 72064c6abb442bfa84cc89e0f00fb50c3a9ffa6c 

# Make changes to the configuration files.
# Set default timeouts 
RUN sed -i.bak 's/askTimeout = .*/askTimeout = 1200/' /nlp/reach/main/src/main/resources/application.conf
# Listen on host 0.0.0.0 
RUN sed -i.bak 's/localhost/0\.0\.0\.0/' /nlp/reach/export/src/main/resources/reference.conf

# Compile a FAT JAR configured to run the file processor server
RUN sbt -DmainClass=org.clulab.reach.export.server.ApiServer assembly

EXPOSE 8080
COPY sbt.sh /

# Run as unprivileged pcuser
RUN adduser --system --home /home/pcuser --shell /bin/bash --group pcuser
RUN chown pcuser:pcuser /nlp/reach/target/scala-2.11/reach-1.3.5-SNAPSHOT-FAT.jar
USER pcuser
RUN mkdir -p /home/pcuser/Documents/reach

WORKDIR /nlp/reach/target/scala-2.11
CMD ["/sbt.sh"]
