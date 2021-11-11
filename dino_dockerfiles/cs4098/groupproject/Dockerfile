FROM ubuntu:12.04
MAINTAINER Cathal Geoghegan <geogheca@tcd.ie>
RUN apt-get update && apt-get install -y build-essential
RUN apt-get install -y python-pip
RUN apt-get install -y python-lxml
RUN apt-get install -y curl
RUN apt-get install -y git
RUN apt-get install -y mercurial
RUN curl http://spinroot.com/spin/Bin/spin643_linux64.gz -o /bin/spin.gz && gunzip /bin/spin.gz && chmod +x /bin/spin
RUN apt-get install -y ghc ghc-prof ghc-doc
RUN apt-get install -y zlib1g-dev
RUN apt-get install -y cabal-install
RUN cabal update
RUN apt-get install -y alex
RUN apt-get install -y happy
RUN apt-get install -y apache2
RUN apt-get install -y default-jdk
RUN cabal install cabal cabal-install
RUN echo 'export PATH=/root/.cabal/bin:$PATH' >> ~/.bashrc
RUN apt-get install -y vim
