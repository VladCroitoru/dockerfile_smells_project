FROM node:9.8.0-stretch
LABEL maintainer="kuzma.wm@gmail.com"

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
  && apt-get update -y \
  && apt-get install google-chrome-stable -y \
  && apt-get clean \
  && rm -rf /tmp/* /var/lib/apt/lists/*

# Add Chrome as a user
RUN groupadd -r chrome && useradd -r -g chrome -G audio,video chrome \
    && mkdir -p /home/chrome && chown -R chrome:chrome /home/chrome

WORKDIR /home/chrome
COPY . /home/chrome
RUN  npm install && chown -R chrome:chrome /home/chrome/

# Run Chrome non-privileged
USER chrome

EXPOSE 3000

CMD [ "node", "server.js" ]

