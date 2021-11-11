FROM node:10.13.0

ENV npm_config_loglevel warn

#
# Install Java
#

RUN apt-get update && apt-get install -y openjdk-7-jre

#
# https://github.com/broadinstitute/docker-terraform/blob/master/Dockerfile
#

ENV TERRAFORM_VERSION=0.11.11

RUN apt-get update && apt-get install -y jq unzip rsync

RUN cd /tmp && \
	wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
	unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/bin && \
	rm -rf /tmp/*

# 
# Install Heroku
# 
RUN wget -qO- https://cli-assets.heroku.com/install-ubuntu.sh | sh

#
# Install binaries to support puppeteer (it's possible that not all are necessary, but 
# I don't know which those would be)
#
RUN apt-get update && apt-get install -y libxss1 libappindicator1 libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 gconf-service lsb-release wget xdg-utils fonts-liberation

