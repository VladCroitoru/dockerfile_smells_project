FROM ruby:2.6.3

ENV PHANTOM_VERSION phantomjs-2.1.1-linux-x86_64
ENV NVM_DIR /nvm
ENV NODE_VERSION 7.4.0
ENV PRAX_DOMAINS=dev,me
RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc"

RUN curl -L -s https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_VERSION.tar.bz2 | tar xj && \
    mv $PHANTOM_VERSION/bin/phantomjs /usr/local/bin/ && rm -rf $PHANTOM_VERSION/

RUN apt-get update && \
    apt-get install -y build-essential \
    libicu-dev \
    postgresql-client libpq-dev redis-tools && \
    rm -rf /var/lib/apt/lists/*

RUN wget -q https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz -O wkhtmltox.tar.xz && \
    tar xf wkhtmltox.tar.xz && \
    mv wkhtmltox/bin/* /usr/local/bin/ && \
    rm -Rf wkhtmltox*

RUN curl -s -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash && \
    . $NVM_DIR/nvm.sh && \
    nvm install $NODE_VERSION && nvm alias default $NODE_VERSION

RUN wget -q https://github.com/yarnpkg/yarn/releases/download/v0.24.5/yarn-v0.24.5.tar.gz -O yarn.tar.gz && \
    tar xf yarn.tar.gz && \
    mv ./dist/bin/* /usr/local/bin/ && \
    rm -Rf ./yarn.tar.gz ./dist

COPY ./ext /ext
RUN cd /ext && make && make install && sed -i "s/hosts:.*/hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4 prax/" /etc/nsswitch.conf && rm -rf /ext
