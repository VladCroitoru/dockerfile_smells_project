# Event Data Visitor

FROM clojure:lein-2.8.1
MAINTAINER Joe Wass jwass@crossref.org
LABEL name="chrome-headless" \ 
      maintainer="Justin Ribeiro <justin@justinribeiro.com>" \
      version="1.4" \
      description="Google Chrome Headless in a container"

# Install deps + add Chrome Stable + purge all the things
RUN apt-get update && apt-get install -y \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg \
  --no-install-recommends \
  && curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update && apt-get install -y \
  google-chrome-stable \
  --no-install-recommends \
  && apt-get purge --auto-remove -y curl gnupg \
  && rm -rf /var/lib/apt/lists/*

# Add Chrome as a user
RUN groupadd -r chrome && useradd -r -g chrome -G audio,video chrome \
    && mkdir -p /home/chrome && chown -R chrome:chrome /home/chrome

RUN usermod -u 1000 chrome

COPY src /usr/src/app/src
COPY test /usr/src/app/test
COPY project.clj /usr/src/app/project.clj

# Need to be non-root for Chrome sandbox.
USER chrome

WORKDIR /usr/src/app

RUN lein deps

