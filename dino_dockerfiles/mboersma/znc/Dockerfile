# mboersma/znc

FROM ubuntu:14.04
MAINTAINER Matt Boersma <matt@sprout.org>

ENV DEBIAN_FRONTEND noninteractive

# install ZNC build prerequisites
RUN apt-get update && \
	apt-get install -yq --force-yes coreutils g++ libssl-dev make

# build and install ZNC
ADD http://znc.in/releases/znc-1.6.0.tar.gz /opt/
RUN cd /opt && tar xzvf znc-1.6.0.tar.gz
RUN cd /opt/znc-1.6.0 && ./configure && make && make install

# clean up after the build
RUN rm -rf znc-1.6.0*
RUN apt-get remove -yq g++ libssl-dev make
RUN apt-get autoremove -yq && apt-get clean

# run ZNC as an unprivileged user
RUN useradd -m -d /opt/znc znc
COPY run /opt/znc/run
RUN chmod +x /opt/znc/run
RUN chown -R znc:znc /opt/znc

# run thie image as a ZNC server
USER znc
WORKDIR /opt/znc
CMD ["/opt/znc/run"]
