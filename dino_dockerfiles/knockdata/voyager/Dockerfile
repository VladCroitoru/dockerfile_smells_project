FROM debian

RUN apt-get update &&  apt-get install -y curl vim gnupg

RUN curl -sL https://deb.nodesource.com/setup_9.x | bash - 

RUN apt-get install -y nodejs git libcairo2-dev libjpeg-dev libgif-dev build-essential



RUN git clone https://github.com/rockie-yang/voyager.git

# Install yarn using npm, due to https://github.com/yarnpkg/yarn/issues/2821
RUN npm install -g yarn \
	&& cd /voyager \
	&& yarn \
	&& yarn build \

RUN yarn cache clean \
	&& apt-get clean autoclean \
  	&& apt-get autoremove -y --force-yes \
  	&& rm -rf /tmp/* \
  	&& rm -rf ~/.m2 ~/.npm ~/.cache \
  	&& rm -rf /var/lib/{apt,dpkg,cache,log}/

WORKDIR /voyager

EXPOSE 9000

CMD ["yarn", "start"]	
