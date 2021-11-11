FROM neurodebian:jessie
MAINTAINER Yaroslav Halchenko <debian@onerussian.com>

USER root

# Speed up installation using our apt cacher - modify conf/etc/apt/apt.conf.d/99apt-cacher if you have any
RUN mkdir -p /etc/apt/apt.conf.d/
COPY conf/etc/apt/apt.conf.d/99apt-cacher /etc/apt/apt.conf.d/99apt-cacher
RUN chmod a+r /etc/apt/apt.conf.d/99apt-cacher

# Make deb-src avail
# RUN sed -i -e 's,^deb\(.*\),deb\1\ndeb-src\1,g' /etc/apt/sources.list.d/neurodebian.sources.list /etc/apt/sources.list

# Make contrib and non-free avail for FSL
RUN sed -i -e 's, main$, main contrib non-free,g' /etc/apt/sources.list.d/neurodebian.sources.list

# Assure popcon doesn't kick in
RUN bash -c "echo 'debconf debconf/frontend select noninteractive' | debconf-set-selections -"

RUN apt-get update
# Use bash for extended syntax
RUN apt-get install -y -q eatmydata
# Some rudimentary tools if we need to do anything within docker and curl and unzip needed for setting up conda
RUN bash -c "eatmydata apt-get install -y -q vim less man-db curl unzip bzip2"
# Run additional lines, primarily to setup/enable snapshots repository etc
RUN bash -c "sed -i -e 's,http://neuro.debian.net/debian/* ,http://snapshot-neuro.debian.net:5002/archive/neurodebian/20170410T000000Z/ ,g' etc/apt/sources.list.d/neurodebian.sources.list"
RUN bash -c "curl -s http://neuro.debian.net/_files/knock-snapshots;"
RUN bash -c "eatmydata apt-get update; eatmydata apt-get dist-upgrade -y;"
# We might be just fine with the core here
RUN bash -c "eatmydata apt-get install -y -q fsl-core fsl-first-data fsl-mni152-templates"

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /boot /media /mnt /srv

# Setting up conda environment given simple_workflow specifications
RUN mkdir /opt/repronim && mkdir /opt/repronim/simple_workflow && \
    mkdir /opt/repronim/simple_workflow/scripts
WORKDIR /opt/repronim/
# RUN curl -Ok https://raw.githubusercontent.com/ReproNim/simple_workflow/e4063fa95cb494da496565ec27c4ffe8a4901c45/Simple_Prep.sh
COPY Simple_Prep.sh ./
WORKDIR /opt/repronim/simple_workflow/scripts
COPY environment.yml ./
COPY expected_output expected_output
COPY *.py ./
WORKDIR /opt/repronim/
RUN bash Simple_Prep.sh

WORKDIR /opt/repronim/simple_workflow/scripts
COPY startup.sh ./
RUN chmod +x startup.sh
ENTRYPOINT ["/opt/repronim/simple_workflow/scripts/startup.sh"]
