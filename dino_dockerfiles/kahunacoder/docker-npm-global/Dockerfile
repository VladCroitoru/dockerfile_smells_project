FROM node:6.9

MAINTAINER "Gary Smith" <docker@kc.gs>

WORKDIR /app

RUN apt-get update \
	&& apt-get install -y build-essential \
	&& apt-get install -y libnotify-bin \
	&& apt-get install -y notify-osd \
	&& apt-get install -y php5-cli \

	&& npm install -g forever \
	&& npm install -g forever-monitor \
	&& npm install -g cordova \
	&& npm install -g phonegap \
	&& npm install -g handlebars \
	&& npm install -g stylus \
	&& npm install -g sass \
	&& npm install -g less \
	&& npm install -g nib \
	&& npm install -g canvas \
	&& npm install -g db2md \
	&& npm install -g browser-sync \
	&& npm install -g browserify \
	&& npm install -g watchify \
	&& npm install -g gulp \
	&& npm install -g rimraf \
	&& npm install -g csslint \
	&& npm install -g eslint \
	&& npm install -g jshint \
	&& npm install -g stylint \
	&& npm install -g yarn

VOLUME ["/app"]
CMD ["npm", "install"]

