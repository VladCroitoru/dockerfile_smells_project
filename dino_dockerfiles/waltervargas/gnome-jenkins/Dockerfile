FROM jenkins:2.32.3
LABEL maintainer "waltervargas@linux.com"

USER jenkins

# Install Plugins
RUN /usr/local/bin/install-plugins.sh git pipeline-stage-view job-dsl workflow-aggregator blueocean maven-plugin

RUN echo 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state
COPY init.groovy.d/* /usr/share/jenkins/ref/init.groovy.d/
COPY files/* /tmp/
COPY files/gitconfig /var/jenkins_home/.gitconfig

USER root
ENV PACKAGES flatpak flatpak-builder
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >> /etc/apt/sources.list
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update && apt-get -y -t jessie-backports install $PACKAGES && rm -rf /var/lib/apt/lists/*

USER jenkins
RUN flatpak remote-add --user gnome-nightly --from https://sdk.gnome.org/gnome-nightly.flatpakrepo \
  && flatpak install --user gnome-nightly org.gnome.Sdk \
  && flatpak install --user gnome-nightly org.gnome.Platform

WORKDIR /var/jenkins_home

ENV GIT_URL https://github.com/waltervargas/gnome-jenkins.git
ENV GIT_BRANCH master
