FROM		ubuntu:16.04

RUN			apt-get update 
RUN			apt-get -y upgrade
RUN			apt-get -y install python3 python3-pip python3-dev
RUN			apt-get -y install libxml2-dev libxslt-dev zlib1g-dev libffi-dev libxss1 libappindicator1 libindicator7 wget
RUN			wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN			apt-get -y install libnss3-dev libgconf2-4 libasound2 libpango1.0-0 fonts-liberation libcurl3 xdg-utils unzip
RUN			dpkg -i google-chrome*.deb

RUN			apt-get -y install xvfb

RUN			wget -N https://chromedriver.storage.googleapis.com/2.28/chromedriver_linux64.zip
RUN			unzip chromedriver_linux64.zip

RUN			chmod +x chromedriver
RUN			mv -f chromedriver /usr/local/share/chromedriver
RUN			ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
RUN			ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
