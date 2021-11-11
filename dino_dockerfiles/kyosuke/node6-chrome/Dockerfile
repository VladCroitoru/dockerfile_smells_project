FROM node:6

# Install Chrome and aws-cli
RUN curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
  && apt-get update && apt-get install -y \
  python-dev \
  google-chrome-stable \
  zip \
  && curl https://bootstrap.pypa.io/get-pip.py | python \
  && pip install awscli --upgrade \
  && rm /etc/apt/sources.list.d/google-chrome.list \
  && rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN /usr/bin/google-chrome
