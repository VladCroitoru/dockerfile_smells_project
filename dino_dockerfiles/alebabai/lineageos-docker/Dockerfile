FROM ubuntu:16.04

# Metainformation
LABEL name="lineageos-docker" \
      maintainer="aliaksandr.babai@gmail.com" \
      version="0.3"

ENV DEBIAN_FRONTEND noninteractive

# Arguments defenition
ARG external_dir="include"
ARG internal_dir=".init"
ARG work_dir="android"
ARG shared_dir="shared"
ARG user="docker-buildbox"

# Environment variables defenition (do not rearrange!)
ENV USER=$user
ENV USER_HOME=/home/$USER
ENV SHARED_DIR=$USER_HOME/$shared_dir
ENV WORK_DIR=$USER_HOME/$work_dir
ENV CCACHE_DIR=$WORK_DIR/.ccache
ENV INIT_DIR=$USER_HOME/$internal_dir
ENV OUT_DIR=$WORK_DIR/out

# Install commons build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-utils \
    bc \
    bison \
    build-essential \
    curl \
    flex \
    g++-multilib \
    gcc-multilib \
    git \
    gnupg \
    gperf \
    imagemagick \
    lib32ncurses5-dev \
    lib32readline-dev \
    lib32z1-dev \
    libesd0-dev \
    liblz4-tool \
    libncurses5-dev \
    libsdl1.2-dev \
    libssl-dev \
    libwxgtk3.0-dev \
    libxml2 \
    libxml2-utils \
    lzop \
    openjdk-8-jdk \
    pngcrush \
    rsync \
    schedtool \
    squashfs-tools \
    unzip \
    xsltproc \
    zip \
    zlib1g-dev

# Install additional useful stuff
RUN apt-get install -y --no-install-recommends \
    bash-completion \
    bsdmainutils \
    ccache \
    file \
    mc \
    nano \
    rsync \
    screen \
    screenfetch \
    ssh \
    sudo \
    tig \
    wget

# Add new user
RUN useradd -ms /bin/bash $USER && \
    echo "$USER ALL=NOPASSWD: ALL" > /etc/sudoers.d/$USER

# Initialize environment
ADD $external_dir $INIT_DIR
RUN mkdir -p $USER_HOME/bin && \
    curl https://storage.googleapis.com/git-repo-downloads/repo > /home/$user/bin/repo && \
    chmod a+x $USER_HOME/bin/repo && \
    wget -P $INIT_DIR https://dl.google.com/android/repository/platform-tools-latest-linux.zip && \
    unzip $INIT_DIR/platform-tools-latest-linux.zip -d $INIT_DIR && \
    mkdir -p $SHARED_DIR && \
    mkdir -p $CCACHE_DIR && \
    mkdir -p $OUT_DIR && \
    chmod -R 775 $USER_HOME && \
    chown -R $USER:$USER $USER_HOME && \
    echo "source $INIT_DIR/startup.sh" >> $USER_HOME/.profile

# Volumes defenition
VOLUME $SHARED_DIR
VOLUME $WORK_DIR
VOLUME $CCACHE_DIR
VOLUME $OUT_DIR

# Configure start up
USER $USER
WORKDIR $WORK_DIR
ENTRYPOINT ["/bin/bash"]
CMD ["-l"]
