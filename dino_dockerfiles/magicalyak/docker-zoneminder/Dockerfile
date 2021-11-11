FROM ubuntu:xenial
MAINTAINER Markos Vakondios <mvakondios@gmail.com> Riley Schuit <riley.schuit@gmail.com>

# Resynchronize the package index files
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    apache2 \
    build-essential \
    cmake \
    dh-autoreconf \
    dpatch \
    git \
    libapache2-mod-php \
    libarchive-zip-perl \
    libavcodec-dev \
    libavdevice-dev \
    libavfilter-dev \
    libavformat-dev \
    libavresample-dev \
    libav-tools \
    libavutil-dev \
    libbz2-dev \
    libcurl4-gnutls-dev \
    libdate-manip-perl \
    libdbd-mysql-perl \
    libdbi-perl \
    libdevice-serialport-perl \
    libgcrypt-dev \
    libgnutls-openssl-dev \
    libjpeg-turbo8 \
    libjpeg-turbo8-dev \
    libmime-lite-perl \
    libmime-perl \
    libmp4v2-dev \
    libmysqlclient-dev \
    libnet-sftp-foreign-perl \
    libnetpbm10-dev \
    libpcre3 \
    libpcre3-dev \
    libpolkit-gobject-1-dev \
    libpostproc-dev \
    libssl-dev \
    libswscale-dev \
    libsys-cpu-perl \
    libsys-meminfo-perl \
    libsys-mmap-perl \
    libtheora-dev \
    libtool \
    libv4l-dev \
    libvlc5 \
    libvlccore8 \
    libvlccore-dev \
    libvlc-dev \
    libvorbis-dev \
    libvpx-dev \
    libwww-perl \
    libjson-any-perl \
    libjson-maybexs-perl \
    libnumber-bytes-human-perl \
    libsoap-wsdl-perl \
    libio-socket-multicast-perl \
    libphp-serialization-perl \
    libimage-info-perl \
    liburi-encode-perl \
    libdata-dump-perl \
    libclass-std-fast-perl \
    libdigest-sha-perl \
    libdata-uuid-perl \
    libfile-slurp-perl \
    perl-modules \
    libx264-dev \
    mysql-client \
    mysql-server \
    php \
    php-cli \
    php-gd \
    php-mysql \
    ssmtp \
    software-properties-common \
    vlc-data \
    yasm \
    zip \
    && add-apt-repository -y ppa:iconnor/zoneminder \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    php-apcu-bc \
    && rm -rf /var/lib/apt/lists/*

# Get the latest master branch and submodule(s)
RUN git clone --recursive https://github.com/ZoneMinder/ZoneMinder

# Change into the ZoneMinder directory
WORKDIR /ZoneMinder

# Configure ZoneMinder
RUN cmake .

# Build & install ZoneMinder
RUN make && make install

# ensure writable folders
RUN ./zmlinkcontent.sh

# Set our volumes before we attempt to configure apache
VOLUME /var/lib/zoneminder/events /var/lib/mysql /var/log/zm

# Stop Apache and Mysql before we configure them
RUN service mysql stop && service apache2 stop

# Configure Apache
RUN cp misc/apache.conf /etc/apache2/sites-available/000-default.conf
RUN echo "ServerName localhost" > /etc/apache2/conf-available/servername.conf && a2enconf -q servername
RUN a2enmod -q rewrite && a2enmod -q cgi

# Configure mysql
# No longer needed for zm >= 1.32.0
#RUN echo "sql_mode=NO_ENGINE_SUBSTITUTION" >> /etc/mysql/mysql.conf.d/mysqld.cnf

# Expose http port
EXPOSE 80

# Get the entrypoint script and make sure it is executable
ADD https://raw.githubusercontent.com/ZoneMinder/zmdockerfiles/master/utils/entrypoint.sh /usr/local/bin/
RUN chmod 755 /usr/local/bin/entrypoint.sh

# This is run each time the container is started
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]