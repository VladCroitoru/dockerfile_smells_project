# Shamelessly copied mostly from https://github.com/justinribeiro/dockerfiles/blob/master/chrome-headless/Dockerfile
FROM  debian:sid
LABEL name="chrome-headless with nodejs"
LABEL maintainer="Jonathan Bunde-Pedersen <jonathan@cc.au.dk>"
LABEL version="1.0"
LABEL description="Google Chrome Headless in a container with Node"

# Install deps + add Chrome Stable + purge all the things + node 7
RUN   apt-get update && apt-get install -y apt-transport-https ca-certificates curl gnupg --no-install-recommends && \
	    curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
	    echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
	    apt-get update && apt-get install -y google-chrome-beta --no-install-recommends && \
      curl -sL https://deb.nodesource.com/setup_7.x | bash - && \
      apt-get install -y nodejs && \
      apt-get install -y build-essential

# Add Chrome as a user
RUN   groupadd -r chrome && \
      useradd -r -g chrome -G audio,video chrome && \
      mkdir -p /home/chrome && \
      chown -R chrome:chrome /home/chrome

# Run Chrome non-privileged
USER  chrome

# Expose port 9222
EXPOSE  9222

# Autorun chrome headless with no GPU
ENTRYPOINT [ "google-chrome-beta" ]
CMD [ "--headless", "--disable-gpu", "--remote-debugging-address=0.0.0.0", "--remote-debugging-port=9222", "--ignore-certificate-errors", "http://webstrates/$WEBSTRATEID" ]
