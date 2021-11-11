FROM gliderlabs/alpine:3.6
MAINTAINER "Kamil Soule"
LABEL name="Docker image for the Robot Framework http://robotframework.org/ with dependencies for test runs in Firefox, using Xvfb"
# Setting compatible versions of dependencies
ARG SELENIUM=2.53.6
ARG ROBOTFRAMEWORK=2.9.2
ARG SELENIUM2LIBRARY=1.8.0
ARG FIREFOX=52.3.0-r0
# Installing Python Pip, Robot framework, browser and
RUN apk-install bash py-pip dbus ttf-freefont firefox-esr=$FIREFOX \
    xvfb && \
    pip install --upgrade pip && \
    pip install robotframework==$ROBOTFRAMEWORK robotframework-selenium2library==$SELENIUM2LIBRARY selenium==$SELENIUM robotframework-xvfb
# Instaling selenium webdriver for firefox
ARG GECKODRIVER=0.14.0
RUN apk-install curl && \
  curl -SLO "https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER/geckodriver-v$GECKODRIVER-linux64.tar.gz" && \
  tar xfz  "geckodriver-v$GECKODRIVER-linux64.tar.gz" -C /usr/bin/ && \
  rm "geckodriver-v$GECKODRIVER-linux64.tar.gz" 
ADD test-runner.sh /usr/local/bin/test-runner.sh
RUN chmod +x /usr/local/bin/test-runner.sh
CMD ["test-runner.sh"]