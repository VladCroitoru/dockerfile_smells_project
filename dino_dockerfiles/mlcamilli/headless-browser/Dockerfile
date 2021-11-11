FROM ubuntu:14.04.4

RUN apt-get update
RUN apt-get install -y chromium-browser python3-pip python3-dev git
RUN apt-get install -y unzip wget xvfb nodejs-legacy npm

# Install Firefox
RUN apt-get install -y libgtk-3-0 libasound2 libdbus-glib-1-2
RUN wget https://ftp.mozilla.org/pub/firefox/releases/46.0.1/linux-x86_64/en-US/firefox-46.0.1.tar.bz2
RUN tar -C /opt/ -xvf firefox-46.0.1.tar.bz2
RUN ln -s /opt/firefox/firefox /usr/bin/firefox

# Install ChromeDriver
RUN wget http://chromedriver.storage.googleapis.com/2.19/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip -d /usr/bin/
RUN chmod a+x /usr/bin/chromedriver

RUN npm install -g phantomjs
ADD . /tmp/
WORKDIR /tmp/
RUN python3 setup.py install
