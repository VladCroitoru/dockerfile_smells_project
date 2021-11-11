FROM debian:stretch
RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -
RUN apt-get install -y \
	make \
	python \
	nodejs \
	graphicsmagick \
	git \
	bzip2 \
	sudo \
	build-essential \
	&& apt-get clean
RUN groupadd node && useradd -g node node && adduser node sudo
RUN mkdir -p /home/node && chown -R node:node /home/node
CMD ["node", "-v"]
