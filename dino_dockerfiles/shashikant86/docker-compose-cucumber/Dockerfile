FROM ruby:2.2.0
MAINTAINER Shashikant jagtap <shashikant.jagtap@aol.co.uk>

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev openjdk-7-jre-headless lib32z1 lib32ncurses5 g++-multilib
RUN apt-get update
RUN apt-get install -y wget

# Main Android SDK
RUN wget -qO- "http://dl.google.com/android/android-sdk_r23.0.2-linux.tgz" | tar -zxv -C /opt/
RUN echo y | /opt/android-sdk-linux/tools/android update sdk --all --filter platform-tools,build-tools-20.0.0 --no-ui --force

ENV ANDROID_HOME /opt/android-sdk-linux

RUN apt-get -y install nodejs
RUN apt-get install -y python-software-properties python g++ make
RUN apt-get install -y bash curl git patch bzip2 build-essential openssl libreadline6 libreadline6-dev curl git-core zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt-dev autoconf libc6-dev libgdbm-dev ncurses-dev automake libtool bison subversion pkg-config libffi-dev libcurl3-dev imagemagick libmagickwand-dev libpcre3-dev
RUN apt-get install -y wget
RUN apt-get install -y nodejs
RUN apt-get install -y npm
RUN apt-get install -y git
RUN apt-get install -y curl
RUN apt-get install -y unzip
RUN apt-get install -y android-tools-adb
RUN apt-get install -y openjdk-7-jre-headless lib32z1 lib32ncurses5 g++-multilib
RUN apt-get install -y vim
RUN apt-get -y install nodejs-legacy
RUN apt-get install -y curl patch gawk g++ gcc make libc6-dev patch libreadline6-dev zlib1g-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 autoconf libgdbm-dev libncurses5-dev automake libtool bison pkg-config libffi-dev

RUN npm install -g phantomjs
# Install Chrome WebDriver
RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    rm /tmp/chromedriver_linux64.zip && \
    chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
    ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver

# Install Google Chrome
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get -yqq update && \
    apt-get -yqq install google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*


RUN mkdir /opt/appium
RUN useradd -m -s /bin/bash appium
RUN chown -R appium:appium /opt/appium

#USER appium
#ENV HOME /home/appium

#RUN cd /opt/appium && npm install appium

EXPOSE 4723
CMD /opt/appium/node_modules/appium/bin/appium.js

RUN mkdir /myapp
WORKDIR /myapp
ADD Gemfile /myapp/Gemfile
RUN bundle install
ADD . /myapp
