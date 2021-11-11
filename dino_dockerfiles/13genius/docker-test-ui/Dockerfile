FROM nodesource/trusty

RUN apt-get update
RUN apt-get install -y curl wget

#
# http://linuxg.net/how-to-fix-error-sudo-add-apt-repository-command-not-found/
#
RUN apt-get install -y software-properties-common

#
# Install git client, jdk
#
RUN apt-get install -y git
RUN apt-get update
RUN apt-get install -y default-jdk

#
# Installing SASS/Compass
# http://ndever.net/articles/linux/installing-sass-and-compass-ubuntu-1210-1304
#
RUN apt-get install -y ruby-full rubygems-integration
RUN gem install sass -v 3.2.19
RUN gem install compass

#
# Install gulp, grunt, bower, protractor
#
RUN npm install -g gulp
RUN npm install -g grunt
RUN npm install -g bower
RUN npm install -g protractor
RUN webdriver-manager update

#
# Install pip
#
RUN apt-get install -y python-pip

#
# Install aws command line interface
#
RUN pip install awscli

###################################################################################################
##
## Selenium / Protractor setup.
##
## There are some special selenium setup to get it to run headless chrome and FF:
## - https://www.exratione.com/2013/12/angularjs-headless-end-to-end-testing-with-protractor-and-selenium/
##
## Also note that unlike many of the example Dockerfiles in DockerHub, we are not standing up
## a persistant selenium instance. We are creating and tearing down a selenium/webdriver instance
## every time a set of integration tests are run.
##
###################################################################################################

#
# Rely on the selenium-standalone npm
# Check out and test selenium-standalone@latest and make sure that the following command:
# - 'docker run --privileged -t -i <current_docker_image> ./testSelenium.sh'
# still succeeds before attempting to update the version number
#
ENV SELENIUM_VERSION 2.53.2
ENV SELENIUM_NPM_VERSION 2.44.0

#
# Create a Xvfb init.d deamon
#
RUN apt-get install -y xvfb
ADD xvfb /etc/init.d/
RUN chown root:root /etc/init.d/xvfb
RUN chmod ugo+x /etc/init.d/xvfb
RUN update-rc.d xvfb defaults

#
# Packages to keep Chrome and FF happy.
#
RUN apt-get install -y x11-xkb-utils xfonts-100dpi xfonts-75dpi
RUN apt-get install -y xfonts-scalable xserver-xorg-core
RUN apt-get update
RUN apt-get install -y dbus-x11

#
# PhantomJS magic.
#
RUN apt-get install -y libfontconfig1-dev

#
# Install Browsers.
#
RUN apt-get install -y chromium-browser firefox
RUN npm install -g phantomjs

#
# Install Selenium and chromedriver.
#
RUN npm install --production selenium-standalone@$SELENIUM_NPM_VERSION -g
RUN npm install -g chromedriver

#
# Setup WORKINGDIR so that docker image can be easily tested.
#
RUN mkdir -p /srcTest
ADD . srcTest
WORKDIR srcTest

RUN chmod ugo+x testSelenium.sh

#
# Install Selenium locally.
#
RUN npm install --production selenium-standalone@$SELENIUM_NPM_VERSION
