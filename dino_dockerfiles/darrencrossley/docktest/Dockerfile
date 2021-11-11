FROM ubuntu

# Dependencies
RUN apt-get update && \
    apt-get -yq install \
    wget git pwgen unzip tar bzip2 \
    libz-dev \
    libsasl2-dev \
    curl vim

# Install Python
RUN apt-get install -yqq python2.7 python-pip python-dev vim python-virtualenv

# Install PhantomJS
RUN apt-get install -yqq phantomjs
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN bzip2 -d phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN tar -xvf phantomjs-2.1.1-linux-x86_64.tar
RUN cp phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/phantomjs

# Install LibSass
RUN apt-get install -yqq libsass-dev


# install nodejs and npm
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs
