FROM ubuntu:xenial
MAINTAINER Tim Cera <tim@cerazone.net>

## for apt to be noninteractive
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

ENV TZ America/New_York

# Need to have apt-transport-https in-place before drawing from
# https://qgis.org
RUN    echo $TZ > /etc/timezone                                              \
    && apt-get -y update                                                     \
    && apt-get -y install --no-install-recommends tzdata                     \
                                                  dirmngr                    \
                                                  apt-transport-https        \
                                                  python-software-properties \
                                                  software-properties-common \
    && add-apt-repository ppa:ubuntugis/ubuntugis-unstable                   \
    && rm /etc/localtime                                                     \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime                        \
    && dpkg-reconfigure -f noninteractive tzdata                             \
    && apt-get clean                                                         \
    && apt-get purge                                                         \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN    echo "deb     https://qgis.org/ubuntugis xenial main" >> /etc/apt/sources.list
RUN    echo "deb-src https://qgis.org/ubuntugis xenial main" >> /etc/apt/sources.list

# Key for qgis ubuntugis
RUN    apt-key adv --keyserver keyserver.ubuntu.com --recv-key CAEB3DC3BDF7FB45

RUN    apt-get -y update                                                 \
    && apt-get -y install --no-install-recommends python-requests        \
                                                  python-numpy           \
                                                  python-pandas          \
                                                  python-scipy           \
                                                  python-matplotlib      \
                                                  python-pyside.qtwebkit \
                                                  gdal-bin               \
                                                  qgis                   \
                                                  python-qgis            \
                                                  qgis-provider-grass    \
                                                  grass                  \
    && apt-get clean                                                     \
    && apt-get purge                                                     \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Called when the Docker image is started in the container
ADD start.sh /start.sh
RUN chmod 0755 /start.sh

CMD /start.sh
