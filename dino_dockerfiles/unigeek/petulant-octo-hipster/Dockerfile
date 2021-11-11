# Set the base image to nepalez/ruby (Ubuntu 14.01 + Ruby + gems + bundler)
# will set WORKDIR to /app
FROM nepalez/ruby

MAINTAINER Mark Halloran

ENV PHANTOM_JS_VERSION 1.9.7-linux-x86_64

# Install rspec, capybara, poltergeist
RUN /bin/bash -l -c 'gem install rspec'
RUN /bin/bash -l -c 'gem install capybara'
RUN /bin/bash -l -c 'gem install poltergeist'

RUN apt-get update -y
RUN add-apt-repository ppa:git-core/ppa
RUN apt-get install -y git 
RUN apt-get install -y curl bzip2 libfreetype6 libfontconfig && \
    apt-get clean
RUN curl -sL https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOM_JS_VERSION.tar.bz2 | tar xj -C /usr/local/share
RUN ln -s /usr/local/share/phantomjs-$PHANTOM_JS_VERSION/bin/phantomjs /usr/local/share/phantomjs
RUN ln -s /usr/local/share/phantomjs-$PHANTOM_JS_VERSION/bin/phantomjs /usr/local/bin/phantomjs
RUN ln -s /usr/local/share/phantomjs-$PHANTOM_JS_VERSION/bin/phantomjs /usr/bin/phantomjs

RUN git clone https://github.com/unigeek/petulant-octo-hipster
WORKDIR /app/petulant-octo-hipster

# Set the default command to execute
CMD ["bash"] 
