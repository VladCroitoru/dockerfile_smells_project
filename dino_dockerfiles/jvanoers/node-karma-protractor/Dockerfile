FROM node:7

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' 

RUN apt-get update && \
    DEBIAN_FRONTEND="noninteractive" \
    apt-get install -y --no-install-recommends \
    google-chrome-stable \
    libgconf-2-4 \
    openjdk-7-jre-headless \
    && rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN /usr/bin/google-chrome