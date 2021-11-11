FROM ubuntu:17.10

RUN \
    # install packages dependencies
    apt-get update -yqq \
    && apt-get install -yqq \
        curl \
        git \
        locales \
        wget \
        squashfs-tools \
        dh-autoreconf \
        build-essential \
        python-pip \
        python3-pip \
        python2.7 \
        python3.6 \
        uuid-runtime \
        libarchive-dev \
    && apt-get clean \
    \
    # configure locale, see https://github.com/rocker-org/rocker/issues/19
    && echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
    && locale-gen en_US.utf8 \
    && /usr/sbin/update-locale LANG=en_US.UTF-8 \
    \
    # Install singularity
    && SOURCE=/tmp/singularity_source \
    && git clone https://github.com/singularityware/singularity.git $SOURCE \
    && cd $SOURCE \
    && git checkout tags/2.6.1 \
    && ./autogen.sh \
    && ./configure \
    && make install \
    && rm -rf $SOURCE

# set locales
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8

# mount the output volume as persistant
ENV OUTPUT_DIR /data
VOLUME ${OUTPUT_DIR}

# install register_apps
COPY . /code
RUN \
    pip3 install /code \
    && rm -rf /code \
    && /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh"

# add entry point
ENTRYPOINT ["register_toil"]
CMD ["--help"]

