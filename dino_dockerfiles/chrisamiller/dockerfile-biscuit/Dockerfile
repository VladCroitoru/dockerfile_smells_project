FROM zackramjan/biscuit
MAINTAINER "Chris Miller" <c.a.miller@wustl.edu>

############################
# java stuff for picard #
ENV JAVA_VERSION=8
# Install necessary packages including java 8 jre and clean up apt caches
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >> /etc/apt/sources.list.d/webupd8team-java.list && \
    echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >> /etc/apt/sources.list.d/webupd8team-java.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 && \
    echo debconf shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    echo debconf shared/accepted-oracle-license-v1-1 seen true | /usr/bin/debconf-set-selections

RUN apt-get update && apt-get --no-install-recommends install -y --force-yes \
    oracle-java${JAVA_VERSION}-installer && \ 
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/ /var/cache/oracle-jdk${JAVA_VERSION}-installer

#########################
### now picard itself ###
ENV picard_version 2.4.1

# Install ant, git for building
RUN apt-get update && \
    apt-get --no-install-recommends install -y --force-yes \
            git \
            ant && \
            apt-get clean autoclean && \
            apt-get autoremove -y

# Assumes Dockerfile lives in root of the git repo. Pull source files into container
RUN cd /usr/ && git config --global http.sslVerify false && git clone --recursive https://github.com/broadinstitute/picard.git && cd /usr/picard && git checkout tags/${picard_version}
WORKDIR /usr/picard

# Clone out htsjdk. First turn off git ssl verification
RUN git config --global http.sslVerify false && git clone https://github.com/samtools/htsjdk.git && cd htsjdk && git checkout tags/${picard_version} && cd ..

# Build the distribution jar, clean up everything else
RUN ant clean all && \
    mv dist/picard.jar picard.jar && \
    mv src/scripts/picard/docker_helper.sh docker_helper.sh && \
    ant clean && \
    rm -rf htsjdk && \
    rm -rf src && \
    rm -rf lib && \
    rm build.xml

RUN apt-get install -y libnss-sss
RUN ln -sf /usr/share/zoneinfo/America/Chicago /etc/localtime

#LSF: Java bug that need to change the /etc/timezone.
#     The above /etc/localtime is not enough.
RUN echo "America/Chicago" > /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata

# install R
RUN apt-get update && apt-get install -y r-base littler \
  && find /var/cache/apt /var/lib/apt/lists -type f -print0 | xargs -0 --no-run-if-empty rm -f

RUN apt-get clean autoclean && \
    apt-get autoremove -y

