FROM richbrains/php7-nodejs-npm-grunt-gulp:latest
MAINTAINER e.marchenkov@richbrains.net

RUN curl -sSL https://get.docker.com/ | bash; \
	apt-get install python3.4 -y; \
	curl -O https://bootstrap.pypa.io/get-pip.py; \
	python get-pip.py --user; \
	ln -s ~/.local/bin/pip /usr/local/bin/pip; \
	pip install awscli --upgrade --user; \