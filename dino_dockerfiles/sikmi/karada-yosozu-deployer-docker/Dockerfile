FROM sikmi/awseb-deployer-docker

# ruby install
RUN curl -O http://ftp.ruby-lang.org/pub/ruby/2.3/ruby-2.3.3.tar.gz && \
    tar -zxvf ruby-2.3.3.tar.gz && \
    cd ruby-2.3.3 && \
    ./configure --disable-install-doc && \
    make && \
    make install && \
    cd .. && \
    rm -r ruby-2.3.3 ruby-2.3.3.tar.gz

RUN gem install bundler

# node install
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install nodejs

