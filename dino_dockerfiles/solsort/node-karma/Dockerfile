FROM node:8.5

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update -y && \ 
    apt-get -y install xvfb firefox-esr google-chrome && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/*
