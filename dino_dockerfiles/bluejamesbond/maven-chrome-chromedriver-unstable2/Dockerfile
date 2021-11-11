# rebuilding 2

FROM maven:3.3.9-jdk-8

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

# Set timezone
RUN echo "US/Pacific" > /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata

# Create a default user
RUN useradd automation --shell /bin/bash --create-home

# Install basics
RUN apt-get -yqq update
RUN apt-get -yqq install curl unzip wget xvfb tinywm alsa-utils upower build-essential libssl-dev
RUN apt-get -yqq install fonts-ipafont-gothic xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic

# Browser requirement
RUN mkdir -p /run/user
RUN chmod -R 777 /run/user/

# Install Chrome WebDriver
RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE?1` && \
    mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    rm /tmp/chromedriver_linux64.zip && \
    chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
    ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver

# Install Google Chrome
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -yqq update
RUN apt-get -yqq install google-chrome-stable

# Install Firefox
# RUN curl http://mozilla.debian.net/archive.asc | apt-key add - 
# RUN echo "deb http://security.debian.org/ stretch/updates main" >> /etc/apt/sources.list.d/debian-mozilla.list
# RUN apt-get -yqq update
# RUN apt-get -yqq install firefox-esr

# Install GeckoDriver
RUN curl -L https://github.com/mozilla/geckodriver/releases/download/v0.16.1/geckodriver-v0.16.1-linux64.tar.gz | tar xz -C /usr/local/bin

# Install Opera
ENV CHANNEL stable
ENV OPERA_CHANNEL opera-$CHANNEL
RUN apt-get update 
RUN apt-get install -y ca-certificates wget
RUN echo "deb http://deb.opera.com/${OPERA_CHANNEL}/ stable non-free" > /etc/apt/sources.list.d/opera.list
RUN wget -qO- http://deb.opera.com/archive.key | apt-key add -
RUN apt-get update
RUN apt-get install -y ${OPERA_CHANNEL} --no-install-recommends
    
# Install OperaDriver
RUN curl -L https://github.com/operasoftware/operachromiumdriver/releases/download/v.2.29/operadriver_linux64.zip > operadriver.zip
RUN unzip -p operadriver.zip */operadriver > /usr/local/bin/operadriver
RUN chmod +x /usr/local/bin/operadriver
RUN rm operadriver.zip

# Install Octane
# RUN npm install -g benchmark-octane

# Verify
# RUN firefox --version
RUN google-chrome --version
RUN geckodriver --version
RUN chromedriver --version
RUN opera --version
RUN operadriver --version
# RUN node --version

ENV DBUS_SESSION_BUS_ADDRESS "/dev/null"
ENV MAVEN_OPTS "-Xmx10240M"
ENV CHROMEDRIVER_PORT 4444
ENV CHROMEDRIVER_WHITELISTED_IPS "127.0.0.1"
ENV CHROMEDRIVER_URL_BASE ''
ENV SHELL "/bin/bash"

EXPOSE 4444

WORKDIR /home/automation
