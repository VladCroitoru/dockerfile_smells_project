# galaxy for hutlab

FROM quay.io/bgruening/galaxy:16.04

MAINTAINER FASRC, rchelp@rc.fas.harvard.edu

WORKDIR /galaxy-central


ENV GALAXY_DB_HOST=localhost \
    GALAXY_DB_USER=galaxy \
    GALAXY_DB_PASSWORD=galaxy \
    GALAXY_DB_NAME=galaxy \
    GALAXY_DB_PORT=5432 \
    GALAXY_VIRTUAL_ENV=/galaxy_venv \
    GALAXY_DATABASE_CONNECTION=postgresql://$GALAXY_DB_USER:"$GALAXY_DB_PASSWORD"@$GALAXY_DB_HOST:$GALAXY_DB_PORT/$GALAXY_DB_NAME \
    GALAXY_CONFIG_INTEGRATED_TOOL_PANEL_CONFIG=/export/galaxy-central/integrated_tool_panel.xml \
    ENABLE_TTS_INSTALL=True

COPY ./startup.sh /usr/bin/startup
COPY ./job_conf.xml /galaxy-central/config/job_conf.xml
COPY ./install_galaxy_python_deps.sh /galaxy-central/install_galaxy_python_deps.sh

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 && \
    sh -c "echo deb http://archive.linux.duke.edu/cran/bin/linux/ubuntu trusty/ > /etc/apt/sources.list.d/r_cran.list" && \
    apt-get update -qq && \
    apt-get upgrade -y && \
    apt-get install --no-install-recommends -y python-software-properties software-properties-common \
    texlive-binaries libfreetype6-dev bowtie bowtie2 libhdf5-dev \
    r-base-core r-base-dev r-cran-mvtnorm r-cran-multcomp r-cran-sandwich r-cran-th.data r-cran-zoo r-cran-testthat \
    r-cran-vegan r-cran-gam r-cran-gbm r-cran-pscl r-cran-robustbase \
    ssh libopenmpi-dev openmpi-bin

RUN sudo -H -u galaxy /galaxy-central/install_galaxy_python_deps.sh && \
    chmod +x /usr/bin/startup && \
    chmod g-w /var/log && \
    ln -s /galaxy-central /usr/local/galaxy-dist

RUN apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Mark folders as imported from the host.
VOLUME ["/export/", "/data/", "/var/lib/docker"]

# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy), 9001 (Galaxy report app)
EXPOSE :80
EXPOSE :21
EXPOSE :8800
EXPOSE :9001

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
