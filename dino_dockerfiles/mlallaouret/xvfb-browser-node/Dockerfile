FROM mlallaouret/ubuntu 

MAINTAINER Marc Lallaouret <mlallaouret@gmail.com>

ENV DISPLAY :99

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update \
    && apt-get install -y openjdk-7-jdk xvfb firefox google-chrome-stable  

RUN curl -fsSL https://nodejs.org/dist/v5.5.0//node-v5.5.0-linux-x64.tar.gz | tar xzf - -C /opt

ENV PATH /opt/node-v5.5.0-linux-x64/bin:$PATH
