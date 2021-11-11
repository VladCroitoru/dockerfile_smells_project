FROM yamaszone/phantomjs:2.1.1

MAINTAINER Mazedur Rahman <mazedur.rahman.liton@gmail.com>

RUN npm install \
	karma \
	karma-jasmine \
	jasmine-core \
	karma-chrome-launcher --save-dev \
	karma-phantomjs-launcher --save-dev

RUN npm install -g karma-cli \
	&& npm cache clean

EXPOSE 9876

ENTRYPOINT ["karma"]
