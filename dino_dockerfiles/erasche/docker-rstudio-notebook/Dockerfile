# RStudio container used for Galaxy RStudio Integration
#
# VERSION       0.1.0

FROM ubuntu:14.04

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8

RUN apt-get -qq update && \
    apt-get install --no-install-recommends -y apt-transport-https ca-certificates && \
    echo "deb https://cran.rstudio.com/bin/linux/ubuntu trusty/" >> /etc/apt/sources.list && \
    apt-key adv --keyserver keys.gnupg.net --recv-key 06F90DE5381BA480 && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 51716619E084DAB9 && \
    apt-get -qq update && \
    apt-get install --no-install-recommends -y locales && \
    echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen && \
    locale-gen en_US.UTF-8 && \
    dpkg-reconfigure locales && \
    apt-get install --no-install-recommends -y apt-transport-https \
        r-base r-base-dev dpkg wget psmisc libssl1.0.0 procps sudo \
        libcurl4-openssl-dev curl libxml2-dev nginx python python-pip net-tools \
        lsb-release tcpdump unixodbc unixodbc-dev libmyodbc odbcinst odbc-postgresql \
        texlive-latex-base texlive-extra-utils texlive-fonts-recommended \
        texlive-latex-recommended libapparmor1 libedit2 && \
    pip install bioblend argparse && \
    apt-get autoremove -y  && \
    apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# Build specific
ENV RSTUDIO_VERSION 0.99.903

# Install rstudio-server
RUN wget http://download2.rstudio.org/rstudio-server-${RSTUDIO_VERSION}-amd64.deb && \
    dpkg -i rstudio-server-${RSTUDIO_VERSION}-amd64.deb && \
    rm /rstudio-server-${RSTUDIO_VERSION}-amd64.deb

ADD rsession.conf /etc/rstudio/rsession.conf

# Install packages
COPY ./packages.R /tmp/packages.R
RUN Rscript /tmp/packages.R

# ENV variables to replace conf file from Galaxy
ENV DEBUG=false \
    GALAXY_WEB_PORT=10000 \
    CORS_ORIGIN=none \
    DOCKER_PORT=none \
    API_KEY=none \
    HISTORY_ID=none \
    REMOTE_HOST=none \
    GALAXY_URL=none \
    RSTUDIO_FULL=1

VOLUME ["/import"]
WORKDIR /import/

ADD ./startup.sh /startup.sh
ADD ./monitor_traffic.sh /monitor_traffic.sh
ADD ./proxy.conf /proxy.conf
ADD ./GalaxyConnector /tmp/GalaxyConnector
ADD ./packages-gx.R /tmp/packages-gx.R
ADD ./rserver.conf /etc/rstudio/rserver.conf

# /import will be the universal mount-point for IPython
# The Galaxy instance can copy in data that needs to be present to the Rstudio webserver
RUN chmod +x /startup.sh && \
    Rscript /tmp/packages-gx.R && \
    pip install galaxy-ie-helpers && \
    groupadd -r rstudio -g 1450 && \
    useradd -u 1450 -r -g rstudio -d /import -c "RStudio User" \
        -p $(openssl passwd -1 rstudio) rstudio && \
    chown -R rstudio:rstudio /import

# Must happen later, otherwise GalaxyConnector is loaded by default, and fails,
# preventing ANY execution
COPY ./Rprofile.site /usr/lib/R/etc/Rprofile.site

# Start RStudio
CMD /startup.sh
EXPOSE 80
