FROM debian:jessie

RUN apt-get update && apt-get install wget -y
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install google-chrome-stable -y

RUN set -xe \
    && useradd -u 1000 --shell /bin/bash --no-create-home --home-dir /tmp user

USER user
EXPOSE 9222

ENTRYPOINT ["/opt/google/chrome/chrome", \
  "--interpreter none", \
  "--headless", \
  "--disable-gpu", \
  "--disable-translate", \
  "--disable-extensions", \
  "--disable-background-networking", \
  "--safebrowsing-disable-auto-update", \
  "--disable-sync", \
  "--metrics-recording-only", \
  "--disable-default-apps", \
  "--no-first-run", \
  "--mute-audio", \
  "--hide-scrollbars", \
  "--remote-debugging-address=0.0.0.0", \
  "--remote-debugging-port=9222"]
