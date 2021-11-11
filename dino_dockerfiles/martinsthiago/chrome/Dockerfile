FROM martinsthiago/browser-base
MAINTAINER Thiago Martins <rogue.thiago@gmail.com>

RUN apt update && \
    apt install -y wget && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt update && \
    apt install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

RUN echo chrome-$(google-chrome --version | awk '{print $3}') > /etc/browser

ADD chrome-launcher.sh /opt/google/chrome/google-chrome
RUN chmod +x /opt/google/chrome/google-chrome

CMD google-chrome