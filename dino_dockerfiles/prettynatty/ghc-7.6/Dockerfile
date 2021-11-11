FROM ubuntu:12.04

MAINTAINER Andrey Kuznetsov <fear@loathing.in>
ENV DEBIAN_FRONTEND noninteractive

# Install basis stuff
RUN apt-get update
RUN apt-get -y install software-properties-common python-software-properties

# Add ghc ppa
RUN add-apt-repository ppa:hvr/ghc -y

# Install basic needed packages
RUN apt-get update
RUN apt-get install -y libgmp3-dev zlib1g-dev 

# Install ghc
RUN apt-get install -y ghc-7.6.3

# Install cabal-install
RUN apt-get install -y cabal-install-1.20

# Install build tools
RUN apt-get install -y alex-3.1.3 happy-1.19.3

# Set PATH
ENV PATH /opt/happy/1.19.3/bin:/opt/alex/3.1.3/bin:/opt/ghc/7.6.3/bin:/opt/cabal/1.20/bin:$PATH