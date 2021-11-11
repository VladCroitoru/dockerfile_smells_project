FROM ubuntu:14.04
USER root
RUN apt-get -qq update

# Install prereqs
RUN apt-get --no-install-recommends -y install \
    build-essential \
    openssh-client \
    ca-certificates \
    curl \
    git \
    time \
    libicu-dev \
    libmozjs185-dev \
    python \
    python-software-properties \
    software-properties-common

    
#Install default sbcl for compiling source    
RUN apt-get install -y sbcl    

#Compile SBCL source
RUN echo "cloning sbcl"
RUN git clone git://git.code.sf.net/p/sbcl/sbcl /sbcl
WORKDIR /sbcl
RUN sh make.sh

#Remove default sbcl
RUN apt-get remove -y sbcl

#Install SBCL from source
RUN sh install.sh

#Install quick lisp
RUN mkdir /quicklisp
WORKDIR /quicklisp
ADD etc/install-quicklisp.lisp install-quicklisp.lisp
ADD etc/install-quicklisp.sh install.sh
RUN sh install.sh

#Install swank
RUN mkdir /swank
WORKDIR /swank
ADD etc/start-swank.lisp start-swank.lisp
ADD etc/swank.sh /usr/local/bin/swank

WORKDIR /sbcl


