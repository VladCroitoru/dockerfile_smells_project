FROM jenkins/jenkins:lts
MAINTAINER Cormac Cannon <cormac.cannon@neuromoddevices.com>

USER root

RUN apt-get update && apt-get install -y ruby gcc-multilib git build-essential bzip2 cpio curl python unzip wget

#Ceedling for TDD -- see http://www.throwtheswitch.org/
RUN gem install rake ceedling

#Download and install Microchip XC16 compiler (nicked wholesale from https://github.com/mmitchel/docker-xc16 -- thanks!)
RUN curl -fSL -A "Mozilla/4.0" -o /tmp/xc16.run "http://www.microchip.com/mplabxc16linux" \
    && chmod a+x /tmp/xc16.run \
    && /tmp/xc16.run --mode unattended --unattendedmodeui none \
        --netservername localhost --LicenseType FreeMode --prefix /opt/microchip/xc16 \
    && rm /tmp/xc16.run

#Install an editor
RUN apt-get install -y nano vim

#Restore jenkins user... user is defined in the jenkins:latest Dockerfile from which this is derived, but doesn't appear to be available here
#USER ${user}
USER jenkins


ENV PATH $PATH:/opt/microchip/xc16/bin

