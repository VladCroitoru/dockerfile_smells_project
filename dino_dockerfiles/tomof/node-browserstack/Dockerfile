FROM node:6

RUN curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
  && apt-get update && apt-get install -y \
  python-dev \
  google-chrome-stable \
  zip \
  unzip \
  && curl https://bootstrap.pypa.io/get-pip.py | python \
  && pip install awscli --upgrade \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/* \
  && cd /usr/local/bin \
  && curl -O https://www.browserstack.com/browserstack-local/BrowserStackLocal-linux-x64.zip \
  && unzip BrowserStackLocal-linux-x64.zip \
  && chmod +x BrowserStackLocal \
  && rm BrowserStackLocal-linux-x64.zip

ENV CHROME_BIN /usr/bin/google-chrome

CMD /usr/local/bin/BrowserStackLocal --key ${BROWSERSTACK_ACCESS_KEY}