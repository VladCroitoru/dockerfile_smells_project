FROM      ubuntu

RUN       apt-get update
RUN       apt-get install -y build-essential python wget

RUN       wget http://nodejs.org/dist/v0.10.26/node-v0.10.26.tar.gz
RUN       tar -zxvf node-v0.10.26.tar.gz
RUN       rm node-v0.10.26.tar.gz

WORKDIR   node-v0.10.26

RUN       ./configure
RUN       make
RUN       make install

WORKDIR   ..

RUN       rm -r node-v0.10.26
RUN       apt-get remove -y build-essential python wget
