FROM sikmi/awseb-deployer-docker:v20180222

# ruby install
RUN curl -O http://ftp.ruby-lang.org/pub/ruby/2.5/ruby-2.5.5.tar.gz && \
    tar -zxvf ruby-2.5.5.tar.gz && \
    cd ruby-2.5.5 && \
    ./configure --disable-install-doc && \
    make && \
    make install && \
    cd .. && \
    rm -r ruby-2.5.5 ruby-2.5.5.tar.gz

RUN gem install bundler -v '1.17.1'

# node install
RUN set -ex \
    && apt-get update \
    && apt-get install -y \
               curl \
               apt-transport-https \
               --no-install-recommends \
    \
    && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && curl -sL https://deb.nodesource.com/setup_6.x | bash - \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install \
         yarn \
    && apt-get clean \
    && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*


