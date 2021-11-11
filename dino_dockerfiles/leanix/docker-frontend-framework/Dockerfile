# See: https://github.com/leanix/docker-phantomjs-2
FROM leanix/phantomjs2:master

CMD /bin/bash

ENV PATH ./node_modules/.bin:$PATH
ADD package.json /ff/
    # Get repositories (apt-get update called at end)
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    curl --silent --location https://deb.nodesource.com/setup_4.x | bash - && \
    # Install NodeJS@4.4.0, Java, XVFB, browsers
    apt-get install -y nodejs=4.4.0-1nodesource1~trusty1 build-essential openjdk-7-jre-headless xvfb google-chrome-stable firefox && \
    ln -s /usr/bin/nodejs /usr/sbin/node && \
    # Update npm & install node packages
    npm install -g npm@3.8.1 && \
    cd ff && npm install && \
    # Download Selenium & webdriver
    ./node_modules/.bin/webdriver-manager update && \
    # Clean-up
    apt-get purge -y build-essential && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
