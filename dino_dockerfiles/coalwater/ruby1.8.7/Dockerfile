From kneip/ree-1.8.7-2012.02
RUN gem install bundler --no-rdoc --no-ri
RUN apt-get update -q && \
    apt-get install -qy sqlite3 libsqlite3-dev libmysqlclient-dev \
                        mysql-client nodejs npm fontconfig && \
    rm -rf /var/lib/apt/lists/*
RUN wget -q -O - https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 | tar -C /opt -xj
RUN mkdir /home/circleci
WORKDIR /home/circleci

