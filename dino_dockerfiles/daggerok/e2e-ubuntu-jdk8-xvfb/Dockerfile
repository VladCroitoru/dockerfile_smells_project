FROM daggerok/e2e-ubuntu-jdk8-xvfb:base-v2
LABEL MAINTAINER='Maksim Kostromin <daggerok@gmail.com> https://github.com/daggerok'
ENV DISPLAY=':99' \
    GECKO_DRV_VER='0.21.0' \
    CHROME_DRV_VER='2.41'
# chrome
RUN sudo apt-get update -y \
 && sudo apt-get clean -y \
 && sudo apt-get install --fix-missing -y fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libatk1.0-0 libcairo2 libcups2 libgdk-pixbuf2.0-0 libgtk-3-0 \
    libnspr4 libnss3 libx11-xcb1 libxss1 xdg-utils \
    && wget -O google-chrome-stable.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && sudo dpkg -i google-chrome-stable.deb \
    && rm -rf ./google-chrome-stable.deb
# chrome driver
RUN wget https://chromedriver.storage.googleapis.com/${CHROME_DRV_VER}/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && sudo mv -f chromedriver /usr/bin/ \
    && rm -rf chromedriver_linux64.zip
# firefox
RUN sudo add-apt-repository ppa:mozillateam/firefox-next \
 && sudo apt-get update -y \
 && sudo apt-get install --fix-missing -y firefox
# gecko driver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v${GECKO_DRV_VER}/geckodriver-v${GECKO_DRV_VER}-linux64.tar.gz \
 && tar -xvzf geckodriver* \
 && sudo mv -f geckodriver /usr/bin/ \
 && sudo chmod +x /usr/bin/geckodriver \
 && rm -rf geckodriver-v${GECKO_DRV_VER}-linux64.tar.gz
# cleanup and reduce image size
RUN sudo apt-get autoremove --purge -y \
 && sudo apt-get autoclean -y \
 && sudo apt-get clean -y \
 && rm -rf /tmp/* || true
# docker exec -it
CMD /bin/bash
