FROM ubuntu:12.04

MAINTAINER Markus Plangg <plangg@ifs.tuwien.ac.at.>

# Upgrading Ubuntu
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get upgrade -y

# Install wget
RUN apt-get install -y apt-utils wget ca-certificates ca-certificates-java

# Install Taverna
RUN wget -P '/tmp' 'https://bitbucket.org/taverna/taverna-commandline-product/downloads/taverna-commandline-digitalpreservation-2.5.0-linux_amd64.deb'
RUN dpkg -i /tmp/taverna-commandline-digitalpreservation-2.5.0-linux_amd64.deb
RUN rm /tmp/taverna-commandline-digitalpreservation-2.5.0-linux_amd64.deb


# Install SCAPE components
## Add sources

### Multiverse
RUN echo 'deb http://us.archive.ubuntu.com/ubuntu/ precise multiverse' >> /etc/apt/sources.list.d/multiverse.list
RUN echo 'deb-src http://us.archive.ubuntu.com/ubuntu/ precise multiverse' >> /etc/apt/sources.list.d/multiverse.list
RUN echo 'deb http://us.archive.ubuntu.com/ubuntu/ precise-updates multiverse' >> /etc/apt/sources.list.d/multiverse.list
RUN echo 'deb-src http://us.archive.ubuntu.com/ubuntu/ precise-updates multiverse' >> /etc/apt/sources.list.d/multiverse.list
RUN echo 'deb http://archive.ubuntu.com/ubuntu/ precise-security multiverse' >> /etc/apt/sources.list.d/multiverse.list
RUN echo 'deb-src http://archive.ubuntu.com/ubuntu/ precise-security multiverse' >> /etc/apt/sources.list.d/multiverse.list

### OPF
RUN wget -O - http://ubapt.opf-labs.org/scape-components.gpg.key | apt-key add - 
RUN echo 'deb http://ubapt.opf-labs.org precise-staging main' >> /etc/apt/sources.list.d/opf.list
RUN echo 'deb http://ubapt.opf-labs.org precise main' >> /etc/apt/sources.list.d/opf.list

### Handbrake
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 816950D8
RUN echo 'deb http://ppa.launchpad.net/stebbins/handbrake-releases/ubuntu precise main' >> /etc/apt/sources.list.d/handbrake.list
RUN echo 'deb-src http://ppa.launchpad.net/stebbins/handbrake-releases/ubuntu precise main' >> /etc/apt/sources.list.d/handbrake.list

## Upgrade Ubuntu
RUN apt-get update
RUN apt-get upgrade -y

## Install packages
RUN apt-cache search -n 'digital-preservation.+' | grep -Po 'digital-preservation-.+(?= - )' | grep -v sanselan | grep -v digital-preservation-migration-office-jodconverter-doc2pdf | xargs apt-get install -y --force-yes

## Clean apt cache
RUN apt-get clean

# Create taverna user
RUN groupadd -g 2000 taverna
RUN useradd -u 2000 -g 2000 -ms /bin/bash taverna
USER taverna

CMD ["executeworkflow", "-help"]