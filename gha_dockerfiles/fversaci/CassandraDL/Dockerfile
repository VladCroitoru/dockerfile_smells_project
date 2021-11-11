FROM dhealth/pylibs-toolkit:0.12.2-cudnn

# install cassandra C++ driver
RUN \
    export DEBIAN_FRONTEND=noninteractive \
    && apt-get update -y -q \
    && apt-get install -y libuv1-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/* 

RUN \
    wget 'https://github.com/datastax/cpp-driver/archive/2.16.0.tar.gz' \
    && tar xfz 2.16.0.tar.gz \
    && cd cpp-driver-2.16.0 \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make -j \
    && make install


#install cassandra python driver + some python libraries
RUN \
    pip3 install --upgrade --no-cache pillow \
    && pip3 install --upgrade --no-cache tqdm numpy matplotlib pandas \
         matplotlib pyyaml opencv-python cassandra-driver 

# install some useful tools
RUN \
    export DEBIAN_FRONTEND=noninteractive \
    && apt-get update -y -q \
    && apt-get install -y \
    aptitude \
    bash-completion \
    dnsutils \
    elinks \
    emacs25-nox emacs-goodies-el \
    fish \
    git \
    htop \
    iproute2 \
    iputils-ping \
    ipython3 \
    less \
    mc \
    nload \
    nmon \
    psutils \
    source-highlight \
    ssh \
    sudo \
    tmux \
    vim \
    wget \
    && rm -rf /var/lib/apt/lists/*

########################################################################
# SPARK installation, to test examples
########################################################################
# download and install spark
RUN \
    cd /tmp && wget 'https://downloads.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz' \
    && cd / && tar xfz '/tmp/spark-3.1.2-bin-hadoop3.2.tgz' \
    && ln -s 'spark-3.1.2-bin-hadoop3.2' spark

# Install jdk
RUN \
    export DEBIAN_FRONTEND=noninteractive \
    && apt-get update -y -q \
    && apt-get install -y openjdk-11-jdk

ENV PYSPARK_DRIVER_PYTHON=python3
ENV PYSPARK_PYTHON=python3
EXPOSE 8080
EXPOSE 7077
EXPOSE 4040
########################################################################

########################################################################
# Cassandra server installation, to test examples
########################################################################
RUN \
    cd /tmp && wget 'https://downloads.apache.org/cassandra/4.0.1/apache-cassandra-4.0.1-bin.tar.gz' \
    && cd / && tar xfz '/tmp/apache-cassandra-4.0.1-bin.tar.gz' \
    && ln -s 'apache-cassandra-4.0.1' cassandra

# increase write timeout to 20 seconds
RUN \
    sed -i 's/^\(write_request_timeout_in_ms:\)\(.*\)/\1 20000/' /cassandra/conf/cassandra.yaml

EXPOSE 9042
########################################################################

########################################################################
# Download the Imagenette dataset
########################################################################
WORKDIR /tmp
RUN \
    wget 'https://s3.amazonaws.com/fast-ai-imageclas/imagenette2-320.tgz' \
    && tar xfz 'imagenette2-320.tgz' \
    && rm 'imagenette2-320.tgz'

RUN \
    useradd -m -G sudo -s /usr/bin/fish -p '*' user \
    && sed -i 's/ALL$/NOPASSWD:ALL/' /etc/sudoers \
    && chown -R user.user '/apache-cassandra-4.0.1'

COPY . /home/user/cassandradl
RUN chown -R user.user '/home/user/cassandradl'
WORKDIR /home/user/cassandradl
RUN pip3 install .
USER user
