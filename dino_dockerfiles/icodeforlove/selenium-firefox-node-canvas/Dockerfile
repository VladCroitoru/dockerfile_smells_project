FROM selenium/standalone-firefox:latest

USER root

RUN apt-get update -y && \
	apt-get install --no-install-recommends -y -q \
		build-essential curl git vim

RUN apt-get install --no-install-recommends -y -q libcairo2-dev libjpeg8-dev libpango1.0-dev libgif-dev g++

RUN mkdir /nodejs && curl http://nodejs.org/dist/v5.9.0/node-v5.9.0-linux-x64.tar.gz | tar xvzf - -C /nodejs --strip-components=1

RUN ln -s /nodejs/bin/node /bin/node
RUN ln -s /nodejs/bin/npm /bin/npm