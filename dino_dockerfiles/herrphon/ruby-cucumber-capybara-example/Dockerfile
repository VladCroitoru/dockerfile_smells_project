FROM ruby

# update/upgrade and install needed dependencies for phantomjs
RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y \
        build-essential \
        chrpath \
        libssl-dev \
        libxft-dev \
 && apt-get install -y \
        libfreetype6 libfreetype6-dev \
        libfontconfig1 libfontconfig1-dev

# install phantomjs
RUN cd /tmp \
 && wget -O phantomjs.tar.bz2 "https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2" \
 && tar xvjf phantomjs.tar.bz2 --strip 1 \
 && cp /tmp/bin/phantomjs /usr/local/bin/phantomjs \
 && ls -la /tmp \
 && rm -rf /tmp/*

# && wget -O phantomjs.tar.bz2 "https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2" \


# do a bundle install of the basic stuff
RUN mkdir /code
ADD code/Gemfile       /code
ADD code/Gemfile.lock  /code
RUN cd /code && bundle install

CMD ["bundle", "exec", "cucumber"]

