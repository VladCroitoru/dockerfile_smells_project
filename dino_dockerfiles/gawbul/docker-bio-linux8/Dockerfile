# Dockerfile to build Bio-Linux8
#
# VERSION 0.1

# use ubuntu base image
FROM ubuntu:14.04

# maintained by me
MAINTAINER Steve Moss <gawbul@gmail.com>

# set $HOME env variable
ENV HOME /root

# change to $HOME directory
WORKDIR $HOME

# add negative pin priority to some graphical packages to stop them installing and borking the build
RUN echo "Package: edubuntu*\nPin: release *\nPin-Priority: -1" >> /etc/apt/preferences
RUN echo "Package: gnome*\nPin: release *\nPin-Priority: -1" >> /etc/apt/preferences
RUN echo "Package: gconf*\nPin: release *\nPin-Priority: -1" >> /etc/apt/preferences
RUN echo "Package: kubuntu*\nPin: release *\nPin-Priority: -1" >> /etc/apt/preferences
RUN echo "Package: lubuntu*\nPin: release *\nPin-Priority: -1" >> /etc/apt/preferences
RUN echo "Package: mate*\nPin: release *\nPin-Priority: -1" >> /etc/apt/preferences
RUN echo "Package: qtubuntu*\nPin: release *\nPin-Priority: -1" >> /etc/apt/preferences
RUN echo "Package: ubuntu*\nPin: release *\nPin-Priority: -1" >> /etc/apt/preferences
RUN echo "Package: unity*\nPin: release *\nPin-Priority: -1" >> /etc/apt/preferences
RUN echo "Package: x11*\nPin: release *\nPin-Priority: -1" >> /etc/apt/preferences
RUN echo "Package: xubuntu*\nPin: release *\nPin-Priority: -1" >> /etc/apt/preferences
RUN echo "Package: xserver*\nPin: release *\nPin-Priority: -1" >> /etc/apt/preferences

# change APT sources.list to pull from GB servers
# uncomment some entries and add some other entries
RUN sed -i "s/archive.ubuntu.com/gb.archive.ubuntu.com/" /etc/apt/sources.list
RUN sed -ri "s/^\# (.*trusty-backports.*)/\1 universe multiverse/" /etc/apt/sources.list
RUN sed -ri "s/^\# (.*trusty-security.*)/\1/" /etc/apt/sources.list
ADD bio-linux-sources.txt $HOME/bio-linux-sources.txt
RUN cat $HOME/bio-linux-sources.txt >> /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 16126D3A3E5C1192

# update the system and install some required/useful packages
RUN apt-get update && apt-get -y upgrade && apt-get -y install build-essential sharutils wget vim git mercurial software-properties-common tmux

# pull BL8 upgrade script from nerc server
RUN wget -c http://nebc.nerc.ac.uk/downloads/bl8_only/upgrade8.sh

# replace the mktemp step with current working directory
RUN sed -i 's/mktemp \-d/pwd/' upgrade8.sh

# run script in unpack mode only
RUN UNPACK_ONLY=1 sh upgrade8.sh

# install bio-linux repository keys
RUN dpkg -EGi ./bio-linux-keyring.deb

# add Bio-Linux and CRAN-to-DEB repositories
RUN apt-add-repository -y ppa:nebc/bio-linux && apt-add-repository -y ppa:marutter/c2d4u

# add bio-linux and rstudio cran legacy lists to apt sources
ADD bio-linux-legacy.list /etc/apt/sources.list.d/bio-linux-legacy.list
ADD cran-latest-r.list /etc/apt/sources.list.d/cran-latest-r.list
RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
RUN apt-get update

# pin some additional packages to ensure they update okay
# as per Tim's Bio-Linux upgrade script
RUN orphans=`cat $HOME/pseudo_orphans.txt | egrep -v "^#"` && for p in $orphans ; do for l in "Package: $p" 'Pin: origin ?*' 'Pin-Priority: 1001' '' ; do echo "$l" ; done done > $HOME/pseudo_orphans.pin && echo $orphans | xargs apt-get -y install

# update the system to register new packages
RUN apt-get update && \
apt-get -y --force-yes -o "Dir::Etc::Preferences=$HOME/pseudo_orphans.pin" upgrade && \
apt-get -y --force-yes -o "Dir::Etc::Preferences=$HOME/pseudo_orphans.pin" dist-upgrade

# install bio-linux packages
ENV DEBIAN_FRONTEND noninteractive
ADD rm_from_package_list.txt $HOME/rm_from_package_list.txt
RUN for p in `cat $HOME/rm_from_package_list.txt` ; do sed -ir "/^$p.*/d" $HOME/bl_master_package_list.txt; done
RUN echo 'mysql-server mysql-server/root_password password root' | debconf-set-selections \
&& echo 'mysql-server mysql-server/root_password_again password root' | debconf-set-selections
RUN chmod +x $HOME/bl_install_master_list.sh
# comment this out currently as docker image exceeds 6GB with everything installed
# and the automated build in the Docker Hub times out while waiting for upload
#RUN /bin/bash $HOME/bl_install_master_list.sh

# set default CRAN mirror to 0-Cloud (cran.rstudio.com)
ADD cran-default-repos.txt $HOME/cran-default-repos.txt
RUN cat cran-default-repos.txt >> /etc/R/Rprofile.site

# clean up
#RUN rm *.*
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# create a biolinux user and add to sudo group
RUN useradd -r -m -U -d /home/biolinux -s /bin/bash -c "Bio-Linux User" -p "" biolinux
RUN usermod -a -G sudo biolinux
# turn off password requirement for sudo groups users
RUN sed -i "s/^\%sudo\tALL=(ALL:ALL)\sALL/%sudo ALL=(ALL) NOPASSWD:ALL/" /etc/sudoers

# change to biolinux user
USER biolinux

# change HOME directory
ENV HOME /home/biolinux
WORKDIR $HOME

# create data directory
RUN mkdir -p $HOME/data
VOLUME ['/home/biolinux/data']
