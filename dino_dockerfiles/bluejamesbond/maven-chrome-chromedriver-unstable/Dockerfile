## local dev
## docker build -t ubuntu ./Dockerfile 

FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

# Set timezone
RUN echo "US/Pacific" > /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata

# Create a default user
RUN useradd automation --shell /bin/bash --create-home

# Install basics
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y build-essential libssl-dev
RUN apt-get install -y software-properties-common
RUN apt-get install -y curl unzip wget xvfb

# gdebi-core for easy *.deb installtion (used for chrome below)
RUN apt-get install -y gdebi-core

# Install Java
RUN add-apt-repository ppa:webupd8team/java
RUN apt-get update
RUN apt-get install -y debconf-utils
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections
RUN apt-get install -y oracle-java8-installer maven

# Install NodeJS
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
RUN sudo apt-get install -y nodejs

# Install Octane
RUN npm install benchmark-octane -g
RUN benchmark-octane

# Browser requirement
RUN mkdir -p /run/user
RUN chmod -R 777 /run/user/

# Install Chrome WebDriver
RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    rm /tmp/chromedriver_linux64.zip && \
    chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
    ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver

# Install Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN gdebi ./google-chrome-stable_current_amd64.deb

# Install Firefox
RUN apt-get install -y firefox

# Install GeckoDriver
RUN curl -L https://github.com/mozilla/geckodriver/releases/download/v0.16.1/geckodriver-v0.16.1-linux64.tar.gz | tar xz -C /usr/local/bin

# Install Opera
RUN echo "deb http://deb.opera.com/opera/ stable non-free" >> /etc/apt/sources.list.d/opera.list
RUN wget -O - http://deb.opera.com/archive.key | apt-key add -
RUN apt-get update
RUN apt-get install -y opera

# Install OperaDriver
RUN curl -L https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.29/operadriver_linux64.zip > operadriver.zip
RUN unzip -p operadriver.zip */operadriver > /usr/local/bin/operadriver
RUN chmod +x /usr/local/bin/operadriver
RUN rm operadriver.zip

# RUN firefox --version
RUN firefox --version
RUN geckodriver --version
RUN google-chrome-stable --version
RUN chromedriver --version
RUN opera --version
RUN operadriver --version
RUN node --version
RUN npm --version

ENV DBUS_SESSION_BUS_ADDRESS "/dev/null"
ENV MAVEN_OPTS "-Xmx10240M"
ENV CHROMEDRIVER_PORT 4444
ENV CHROMEDRIVER_WHITELISTED_IPS "127.0.0.1"
ENV CHROMEDRIVER_URL_BASE ''
ENV SHELL "/bin/bash"

EXPOSE 4444

WORKDIR /home/automation
