# Run chrome-headless-screenshots in a container
#
# Based on chrome-headless[1] by Justin Ribeiro
# and chrome-headless-screenshots[2] by David Schnurr
# 
# [1]: https://github.com/justinribeiro/dockerfiles/blob/master/chrome-headless/Dockerfile
# [2]: https://github.com/schnerd/chrome-headless-screenshots

# Base docker image
FROM debian:sid
LABEL name="chromeshot" \ 
    maintainer="Tony Thompson <tony@thompson.name>" \
    version="0.01" \
    description="Google Chrome Headless in a container"

# Install deps + add Chrome Stable + purge all the things
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        apt-transport-https \
        ca-certificates \
        curl \
        git\
        gnupg \
	&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
	&& echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && curl -sL https://deb.nodesource.com/setup_7.x | bash - \
	&& apt-get update && apt-get install -y --no-install-recommends \
	    google-chrome-stable \
        nodejs \
	&& apt-get purge --auto-remove -y curl gnupg \
	&& rm -rf /var/lib/apt/lists/* 

# It's nice to have yarn.
RUN npm install -g yarn && npm cache clean

# Add Chrome as a user
RUN groupadd -r chrome && useradd -r -g chrome -G audio,video chrome \
    && mkdir -p /home/chrome && chown -R chrome:chrome /home/chrome

# Install chrome-headless-screenshots and dependencies
RUN git clone https://github.com/schnerd/chrome-headless-screenshots /chromeshot \
    && cd /chromeshot \
    && yarn install \
    && yarn cache clean 

# Run Chrome non-privileged
USER chrome

# Copy in our working directory.
ADD ./entrypoint.sh /chromeshot/entrypoint.sh

# Start chrome headlessly, and take the chromeshot.
ENTRYPOINT [ "/chromeshot/entrypoint.sh" ]
