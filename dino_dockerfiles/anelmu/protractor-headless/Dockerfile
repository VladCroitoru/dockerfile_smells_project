FROM node:12-stretch
VOLUME /var/lib/docker
WORKDIR /tmp
COPY webdriver-versions.js ./
ENV CHROME_PACKAGE="google-chrome-stable_current_amd64.deb" NODE_PATH=/usr/local/lib/node_modules:/protractor/node_modules
RUN npm install -g protractor@5.4.2 minimist@1.2.0 && \
    node ./webdriver-versions.js && \
    webdriver-manager update && \
	echo "deb [check-valid-until=no] http://cdn-fastly.deb.debian.org/debian jessie main" > /etc/apt/sources.list.d/jessie.list && \
	echo "deb [check-valid-until=no] http://archive.debian.org/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list && \
	sed -i '/deb http:\/\/deb.debian.org\/debian jessie-updates main/d' /etc/apt/sources.list && \
    apt-get -o Acquire::Check-Valid-Until=false update && \
    apt-get install -y xvfb wget sudo && \
    apt-get install -y -t jessie-backports openjdk-8-jre && \
	apt-get install -y bzip2 && \
	apt-get install -y zip && \
	apt-get install -y unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg --unpack ${CHROME_PACKAGE} && \
    apt-get install -f -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* \
    rm ${CHROME_PACKAGE} && \
    mkdir /protractor
COPY protractor.sh /
COPY environment /etc/sudoers.d/
# Fix for the issue with Selenium, as described here:
# https://github.com/SeleniumHQ/docker-selenium/issues/87
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null SCREEN_RES=1280x1024x24
WORKDIR /protractor
ENTRYPOINT ["/protractor.sh"]