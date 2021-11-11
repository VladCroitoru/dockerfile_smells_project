FROM laurentmalvert/docker-boinc
RUN apt-get update \
    && apt-get -y install wget \
    && wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | apt-key add - \
    && echo 'deb http://download.virtualbox.org/virtualbox/debian jessie contrib' >> /etc/apt/sources.list \
    && apt-get update && apt-get -y install virtualbox-5.1
