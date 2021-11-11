FROM python:2.7.13

RUN apt-get update && \
    apt-get install -y zip \
                    unzip \
                    jq \
                    # for chrome packages
                    fonts-noto-cjk fonts-liberation libappindicator3-1 \
                    libasound2 libnspr4 libxtst6 libnss3 libxss1 xdg-utils \
                    --no-install-recommends && \
                    wget -q https://noto-website-2.storage.googleapis.com/pkgs/NotoSerifCJKjp-hinted.zip && \
                    unzip NotoSerifCJKjp-hinted.zip -d /usr/share/fonts/opentype/noto && \
                    rm NotoSerifCJKjp-hinted.zip && \
                    chmod 644 /usr/share/fonts/opentype/noto/* && \
                    rm -rf /var/lib/apt/lists/* && \
                    curl -O https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
                    dpkg -i google-chrome-stable_current_amd64.deb

RUN pip install awsebcli \
                awscli

ENV DOCKER_VERSION=17.03.0-ce
RUN curl -L -o /tmp/docker-${DOCKER_VERSION}.tgz https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz && \
    tar -xz -C /tmp -f /tmp/docker-${DOCKER_VERSION}.tgz && \
    mv /tmp/docker/* /usr/bin

RUN curl https://raw.githubusercontent.com/apex/apex/master/install.sh | sh

# ruby install
RUN curl -O http://ftp.ruby-lang.org/pub/ruby/2.5/ruby-2.5.3.tar.gz && \
    tar -zxvf ruby-2.5.3.tar.gz && \
    cd ruby-2.5.3 && \
    ./configure --disable-install-doc && \
    make && \
    make install && \
    cd .. && \
    rm -r ruby-2.5.3 ruby-2.5.3.tar.gz

RUN gem install bundler -v '1.17.3'

# node install
RUN set -ex \
    && curl -sL https://deb.nodesource.com/setup_6.x | bash - \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install \
       nodejs \
       --no-install-recommends \
    && npm cache clean \
    && npm install n -g \
    && n 6.1.0 \
    && apt-get purge -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# rust install
RUN set -ex \
    && curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH $PATH:~/.cargo/bin    

RUN set -ex \
    && apt-get update  \
    && apt-get install -y \
                    mysql-client \
                    --no-install-recommends  \
    && rm -rf /var/lib/apt/lists/*

