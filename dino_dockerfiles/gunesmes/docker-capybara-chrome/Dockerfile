FROM ruby:2.3

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

# Set timezone
RUN echo "US/Eastern" > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

RUN apt-get update -y && \
  apt-get install -y unzip xvfb \
  qt5-default libqt5webkit5-dev \
  gstreamer1.0-plugins-base \
  gstreamer1.0-tools gstreamer1.0-x \
  freetds-dev \
  libnss3 libxi6 libgconf-2-4

WORKDIR /usr/src/app/

# install required gem files for Capybara
COPY ./Gemfile /usr/src/app/
RUN gem install bundler
RUN bundle install

# install chrome
RUN apt-get update -y && \
  wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
  dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# install chromedriver and place it ib path
RUN wget https://chromedriver.storage.googleapis.com/2.38/chromedriver_linux64.zip && \
  unzip chromedriver_linux64.zip && \
  mv chromedriver /usr/local/bundle/bin/
