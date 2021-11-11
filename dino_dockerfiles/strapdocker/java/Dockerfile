FROM phusion/baseimage:latest

# Install Java
RUN apt-get update
RUN apt-get install -y software-properties-common python-software-properties
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get update
RUN rm /usr/sbin/policy-rc.d
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections
RUN apt-get install -y oracle-java7-installer

CMD ["/sbin/my_init"]