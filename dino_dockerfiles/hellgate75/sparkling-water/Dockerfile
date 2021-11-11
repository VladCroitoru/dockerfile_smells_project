FROM hellgate75/apache-spark

# maintainer details
MAINTAINER Fabrizio Torelli <hellgate75@gmail.com>

ENV DEBIAN_FRONTEND=noninteractive \
    sparklingWaterWesion=2.1.8 \
    SPARKLING_EXECUTORS=1 \
    SPARKLING_EXECUTOR_MEMORY="4g" \
    SPARKLING_EXECUTOR_CORES=1 \
    SPARKLING_DRIVER_MEMORY="4g" \
    SPARKLING_HOME=""

USER root

COPY docker-start-sparkling.sh /usr/local/bin/docker-start-sparkling

COPY run-sparkling.sh /usr/local/bin/run-sparkling

COPY bootstrap.sh /etc/bootstrap.sh


RUN chmod 777 /usr/local/bin/docker-start-sparkling && \
    chmod 777 /usr/local/bin/run-sparkling && \
        chmod 777 /etc/bootstrap.sh

COPY sources.list /etc/apt/sources.backup.list
COPY unofficial.source.list /etc/apt/unofficial.source.list
COPY gpg_keys.txt /etc/apt/gpg_keys.txt
RUN \
#    cat /etc/apt/sources.list >> /etc/apt/sources.backup.list && \
    cat /etc/apt/sources.backup.list > /etc/apt/sources.list && \
    chmod 777 /etc/apt/sources*.list && \
    chmod 777 /etc/apt/gpg_keys.txt

# add a post-invoke hook to dpkg which deletes cached deb files
# update the sources.list
# update/dist-upgrade
# clear the caches
RUN apt-get update && apt-get -y --no-install-recommends --allow-unauthenticated install apt-transport-https && \
    cat /etc/apt/unofficial.source.list >> /etc/apt/sources.list && \
    /etc/apt/gpg_keys.txt && \
    # cat /etc/apt/sources.list | awk '!a[$0]++' > /etc/apt/sources.new.list && \
    # cp /etc/apt/sources.list /etc/apt/sources.old.list && \
    # cp /etc/apt/sources.new.list /etc/apt/sources.list && \
    apt-get -y --allow-unauthenticated upgrade

WORKDIR /opt

RUN echo 'DPkg::Post-Invoke {"/bin/rm -f /var/cache/apt/archives/*.deb || true";};' | tee /etc/apt/apt.conf.d/no-cache && \
    #echo "deb http://mirror.math.princeton.edu/pub/ubuntu trusty main universe" >> /etc/apt/sources.list && \
    add-apt-repository -y ppa:graphics-drivers/ppa && \
    apt-get update -q -y && \
    apt-get dist-upgrade -y && \
  # Install Oracle Java 7
    export DEBIAN_FRONTEND=noninteractive && \
#    sort /etc/apt/sources.list | uniq > /etc/apt/sources.list && \
    #sudo add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main universe restricted multiverse" && \
    DEBIAN_FRONTEND=noninteractive apt-get --no-install-recommends --allow-unauthenticated  install -y vim pciutils linux-headers-4.4.0-21-generic wget unzip python-pip python-setuptools python-sklearn python-pandas python-numpy python-matplotlib software-properties-common python-software-properties && \
    pip install --upgrade pip && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update -q && \
    echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y oracle-java8-installer && \
    apt-get clean && \
    apt-get -y autoclean && \
  #  rm -rf /var/cache/apt/* && \
    rm -rf /var/lib/apt/lists/* && \
  # Fetch h2o latest_stable
    wget http://h2o-release.s3.amazonaws.com/sparkling-water/rel-2.1/8/sparkling-water-${sparklingWaterWesion}.zip -O /opt/h2o-sparkling-water-${sparklingWaterWesion}.zip && \
    unzip -d /opt /opt/h2o-sparkling-water-${sparklingWaterWesion}.zip && \
    rm /opt/h2o-sparkling-water-${sparklingWaterWesion}.zip && \
    export SPARKLING_HOME="/opt/$(ls /opt | grep sparkling)"

# RUN echo "Install CUDA Nvidia drivers ..." && \
#     wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/7fa2af80.pub && \
#     cat 7fa2af80.pub | apt-key add - && \
#     rm 7fa2af80.pub && \
#     wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_8.0.61-1_amd64.deb && \
#     sudo dpkg -i cuda-repo-ubuntu1604_8.0.61-1_amd64.deb && \
#     rm cuda-repo-ubuntu1604_8.0.61-1_amd64.deb && \
#     echo "deb http://ftp.debian.org/debian experimental main" >> /etc/apt/sources.list && \
#     sudo apt-get update && \
#     apt-get --no-install-recommends --allow-unauthenticated  install -y cuda


#Install R
RUN apt-get update && \
    apt-get install -y apt-transport-https && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 && \
    add-apt-repository 'deb [arch=amd64,i386] https://cran.rstudio.com/bin/linux/ubuntu xenial/' && \
    apt-get update && \
    apt-get install -y r-base --no-install-recommends && \
    apt-get clean && \
    apt-get -y autoclean && \
    rm -rf /var/lib/apt/lists/*


ENTRYPOINT ["/bin/bash"]

# Define working directory
WORKDIR $SPARK_HOME

# Define default command
CMD ["docker-start-sparkling", "-daemon"]

VOLUME ["/user/root/data/hadoop/hdfs/datanode", "/user/root/data/hadoop/hdfs/namenode", "/user/root/data/hadoop/hdfs/checkpoint", "/etc/config/hadoop", "/etc/config/spark", "mkdir -p /root/application"]

# Exposed Apache Haddop ports
# Apache Spark ports :
# 8080
# Apache Hadoop HDFS ports :
# 50010 50020 50070 50075 50090 8020 9000
# Apache Hadoop MAP Reduce ports :
# 10020 19888
# Apache Hadoop YARN ports:
# 8030 8031 8032 8033 8040 8042 8088
# Other Apache Hadoop ports:
# 49707 2122
EXPOSE 50010 50020 50070 50075 50090 8020 9000 10020 19888 8030 8031 8032 8033 8040 8042 8088 49707 2122 8080
