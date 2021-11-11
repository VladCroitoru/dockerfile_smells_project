FROM ubuntu:saucy
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -q update && apt-get -q -y install gcc git-core && apt-get clean
ADD https://codeload.github.com/Araq/Nimrod/tar.gz/master /opt/master.tgz
# This is a comment.
RUN ls /
RUN cd /opt && \
    tar -zxvf master.tgz && \
    cd /opt/Nimrod-master && \
    git clone --depth 1 git://github.com/nimrod-code/csources && \    
    cd csources && \
    sh build.sh && \
    cd .. && \
    bin/nimrod c koch && \
    ./koch boot -d:release && \
    ln -s /opt/Nimrod-master/bin/nimrod /usr/bin/nimrod
ADD https://codeload.github.com/nimrod-code/babel/tar.gz/master /opt/babel-master.tgz
RUN cd /opt && \
    tar -zxvf babel-master.tgz && \
    cd babel-master && \
    nimrod c -r src/babel install
ENV PATH /.babel/bin:/usr/lib/ccache:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games 
