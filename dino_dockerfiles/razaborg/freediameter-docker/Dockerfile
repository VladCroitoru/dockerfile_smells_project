FROM ubuntu:trusty
LABEL Maintainer="razaborg"
LABEL Description="An Ubuntu-based and simple Docker image of freeDiameter"

# Environement Variables:
# - TZ: Container timezone (default: Europe/Paris)

# Updating the packages
RUN apt-get update
# Installing the freeDiameter dependencies
RUN apt-get -y install mercurial cmake make gcc g++ bison flex libsctp-dev libgnutls-dev libgcrypt-dev libidn11-dev ssl-cert debhelper fakeroot libpq-dev libmysqlclient-dev libxml2-dev swig python-dev
# Downloading the code

WORKDIR /root 
RUN hg clone http://www.freediameter.net/hg/freeDiameter \
&& mkdir freeDiameter/fDBuild  

# Making the freeDiameter code
WORKDIR /root/freeDiameter/fDBuild 
RUN cmake -DCMAKE_BUILD_TYPE=Debug -DALL_EXTENSIONS=ON -DCMAKE_INSTALL_PREFIX='' ../ \
&& make \
&& make install

# Installing Timezone data and setting up the correct TZ
RUN apt-get -y tzdata
RUN ln -snf /usr/share/zoneinfo/${TZ:-Europe/Paris} /etc/localtime \
&& echo ${TZ:-Europe/Paris} > /etc/timezone


WORKDIR /root
RUN mkdir -p /etc/freeDiameter
COPY freeDiameter.conf /etc/freeDiameter/ 
COPY script.sh /root/
RUN chmod +x /root/script.sh
ENTRYPOINT /root/script.sh

EXPOSE 3868 5658

