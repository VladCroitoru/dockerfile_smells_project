FROM registry.access.redhat.com/ubi8/ubi:latest
MAINTAINER Michael Tipton "mike@ibeta.org"
ENV HOME=/home/app

# Base install packages
#RUN yum -y --setopt=tsflags=nodocs update \
RUN yum -y localinstall https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm

# Make our home/work dir for our app
RUN mkdir $HOME && chgrp -R 0 $HOME && chmod -R g=u $HOME

# Install python from main repos [3.9]
RUN yum -y --setopt=tsflags=nodocs install @python39

# Install chromium and chromedriver
RUN yum -y install --setopt=tsflags=nodocs chromium chromedriver \
    && yum clean all && rm -rf /var/cache/yum

# Add and install pip requirements
ADD ./requirements.txt $HOME
RUN pip3 install --no-cache-dir -r $HOME/requirements.txt \
    && rm $HOME/requirements.txt
USER 1000
ADD ./main.py $HOME
WORKDIR $HOME
