FROM sikmi/awseb-deployer-docker

# ruby install
RUN curl -O http://ftp.ruby-lang.org/pub/ruby/2.4/ruby-2.4.0.tar.gz && \
    tar -zxvf ruby-2.4.0.tar.gz && \
    cd ruby-2.4.0 && \
    ./configure --disable-install-doc && \
    make && \
    make install && \
    cd .. && \
    rm -r ruby-2.4.0 ruby-2.4.0.tar.gz

RUN gem install bundler

