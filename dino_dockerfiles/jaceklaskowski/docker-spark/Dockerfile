# Apache Spark image for Docker
#
# https://github.com/jaceklaskowski/docker-spark
#
# If you're reading this and have any feedback on how this image could be improved,
# please open an issue or a pull request so we can discuss it!

FROM java:8
MAINTAINER Jacek Laskowski <jacek@japila.pl>

ENV SPARK_VERSION 1.6.1
ENV SPARK_DIR     spark-${SPARK_VERSION}-bin-hadoop2.6
ENV SPARK_TGZ     $SPARK_DIR.tgz
ENV SPARK_HOME    /usr/local/spark
ENV ATOM_VERSION  v1.7.3
ENV SBT_VERSION   0.13.11
ENV SBT_TGZ       sbt-$SBT_VERSION.tgz
ENV SBT_HOME      /usr/local/sbt
ENV PATH          $PATH:$JAVA_HOME/bin:$SPARK_HOME/bin:$SBT_HOME/bin

# See https://github.com/phusion/baseimage-docker/issues/58
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# See https://hub.docker.com/r/jamesnetherton/docker-atom-editor/~/dockerfile/
RUN apt-get -y update && \
    apt-get install vim-tiny \
                    git \
                    curl \
                    ca-certificates \
                    libgtk2.0-0 \
                    libxtst6 \
                    libnss3 \
                    libgconf-2-4 \
                    libasound2 \
                    fakeroot \
                    gconf2 \
                    gconf-service \
                    libcap2 \
                    libnotify4 \
                    libxtst6 \
                    libnss3 \
                    gvfs-bin \
                    xdg-utils \
                    python -y --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    wget -qO - http://d3kbcqa49mib13.cloudfront.net/${SPARK_TGZ} | tar -xz -C /usr/local/ && \
    cd /usr/local && ln -s ${SPARK_DIR} spark && \
    useradd -d /home/spark -m spark && \
    chown -R spark:spark $SPARK_DIR && \
    echo -ne "- with Spark $SPARK_VERSION\n" >> /root/.built && \
    curl -L https://github.com/atom/atom/releases/download/${ATOM_VERSION}/atom-amd64.deb > /tmp/atom.deb && \
    dpkg -i /tmp/atom.deb && \
    rm -f /tmp/atom.deb

# Install sbt
RUN curl -sL "http://dl.bintray.com/sbt/native-packages/sbt/$SBT_VERSION/$SBT_TGZ" | tar -xz -C /usr/local && \
    echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built

USER spark

# Clone the Spark Workshop repo and prepare the workspace
WORKDIR /home/spark
RUN git clone https://github.com/jaceklaskowski/spark-workshop.git && \
    cd spark-workshop && \
    sbt test

EXPOSE 4040 8080

WORKDIR /home/spark/spark-workshop

CMD ["/bin/bash"]
