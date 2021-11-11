FROM ubuntu:15.10

MAINTAINER Dmitrii Voitovich <dmitrii.voitovich@cashongo.co.uk>

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true
ENV SCREEN_WIDTH 1600
ENV SCREEN_HEIGHT 900
ENV SCREEN_DEPTH 24
ENV DISPLAY :99.0


ENV TZ "Europe/London"
RUN echo "Europe/London" | tee /etc/timezone \
    && dpkg-reconfigure --frontend noninteractive tzdata


RUN apt-get update -y \
    && apt-get -y --no-install-recommends install ca-certificates openjdk-7-jre sudo unzip wget xvfb lsof \
    && rm -rf /var/lib/apt/lists/*


RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update -y \
  && apt-get -y install google-chrome-stable \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/*


ADD SeleniumGridExtras.jar /opt/selenium/selenium-server-standalone.jar
ADD hub_4444.json /opt/selenium/hub_4444.json
ADD node_5555.json /opt/selenium/node_5555.json
ADD node_5556.json /opt/selenium/node_5556.json
ADD selenium_grid_extras_config.json /opt/selenium/selenium_grid_extras_config.json
ADD entry_point.sh /opt/bin/entry_point.sh

RUN chmod +x /opt/bin/entry_point.sh


EXPOSE 3000

WORKDIR /opt/selenium/

CMD ["/opt/bin/entry_point.sh"]