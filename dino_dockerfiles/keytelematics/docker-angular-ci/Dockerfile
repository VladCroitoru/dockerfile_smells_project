FROM openjdk:8-jre

# from https://github.com/shusson/docker-chrome-headless/blob/master/Dockerfile

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get update && \
    apt-get install -y xvfb wget nodejs && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg --unpack google-chrome-stable_current_amd64.deb && \
    apt-get install -f -y && \
    apt-get clean && \
    rm google-chrome-stable_current_amd64.deb

RUN npm install -g protractor mocha jasmine karma-cli && \
    webdriver-manager update && \
    mkdir /tests

# Fix for the issue with Selenium, as described here:
# https://github.com/SeleniumHQ/docker-selenium/issues/87
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null
WORKDIR /tests

RUN apt-get update && apt-get install python python-pip jq gettext -y && \
	pip install awscli && \
    apt-get remove python-pip -y && \
    apt-get autoclean -y && apt-get clean -y

RUN npm install yarn --global

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]