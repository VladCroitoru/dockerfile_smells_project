FROM ubuntu:16.04
MAINTAINER Arjun Attam

RUN apt-get -y update && apt-get install -y \
    unzip \
    curl \
    wget \
    openjdk-8-jre-headless \
    xvfb \
    fonts-ipafont-gothic \
    xfonts-100dpi \
    xfonts-75dpi \
    xfonts-scalable \
    xfonts-cyrillic

ENV CHROME_PACKAGE="google-chrome-stable_55.0.2883.75-1_amd64.deb"

# Install Chrome
RUN wget https://github.com/webnicer/chrome-downloads/raw/master/x64.deb/${CHROME_PACKAGE} && \
    dpkg --unpack ${CHROME_PACKAGE} && \
    apt-get install -f -y && \
    apt-get clean && \
    rm ${CHROME_PACKAGE}

# Enable WebGL for Chrome
RUN apt-get install libosmesa6
RUN ln -s /usr/lib/x86_64-linux-gnu/libOSMesa.so.6 /opt/google/chrome/libosmesa.so

# Disable the SUID sandbox so that chrome can launch without being in a privileged container
RUN dpkg-divert --add --rename --divert /opt/google/chrome/google-chrome.real /opt/google/chrome/google-chrome
RUN echo "#!/bin/bash\nexec /opt/google/chrome/google-chrome.real --disable-setuid-sandbox \"\$@\"" > /opt/google/chrome/google-chrome
RUN chmod 755 /opt/google/chrome/google-chrome

# Install selenium
RUN mkdir -p /opt/selenium
RUN curl http://selenium-release.storage.googleapis.com/3.4/selenium-server-standalone-3.4.0.jar -o /opt/selenium/selenium-server-standalone.jar

# Install Chrome Driver
RUN curl http://chromedriver.storage.googleapis.com/2.27/chromedriver_linux64.zip -o /opt/selenium/chromedriver_linux64.zip
RUN cd /opt/selenium; unzip /opt/selenium/chromedriver_linux64.zip; rm -rf chromedriver_linux64.zip;

ENV DISPLAY :20
COPY entrypoint.sh /opt/selenium/entrypoint.sh
RUN chmod +x /opt/selenium/entrypoint.sh

EXPOSE 4444
CMD ["sh", "/opt/selenium/entrypoint.sh"]
