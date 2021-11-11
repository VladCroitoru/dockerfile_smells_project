FROM centos:7

# Install requirements
RUN yum -y install sqlite git gcc make wget && \
    wget https://storage.googleapis.com/golang/go1.8.3.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.8.3.linux-amd64.tar.gz

# Setup gopath
RUN mkdir $HOME/go
ENV GOROOT=/usr/local/go
ENV GOPATH=$HOME/go
ENV PATH=$PATH:$GOROOT/bin:$GOPATH/bin

# Build go-cve-dictionary
RUN mkdir -p $GOPATH/src/github.com/kotakanbe && \
    cd $GOPATH/src/github.com/kotakanbe && \
    git clone https://github.com/kotakanbe/go-cve-dictionary.git && \
    cd go-cve-dictionary && \
    make install

# Build goval-dictionary
RUN mkdir -p $GOPATH/src/github.com/kotakanbe && \
    cd $GOPATH/src/github.com/kotakanbe && \
    git clone https://github.com/kotakanbe/goval-dictionary.git && \
    cd goval-dictionary && \
    make install

# Build vuls
RUN mkdir -p $GOPATH/src/github.com/future-architect && \
    cd $GOPATH/src/github.com/future-architect && \
    git clone https://github.com/future-architect/vuls.git && \
    cd vuls && \
    make install
