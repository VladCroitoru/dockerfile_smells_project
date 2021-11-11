FROM python:alpine

MAINTAINER Matt Knight

RUN apk --no-cache add git build-base libffi-dev openssl-dev postgresql-dev autoconf automake nodejs

RUN mkdir -p /www && git clone https://github.com/Netflix/lemur /www/lemur

WORKDIR /www/lemur

RUN python setup.py develop

# we have to install these manually as the installer fails downloading them
RUN npm install imagemin-gifsicle \
                imagemin-jpegtran \
                imagemin-optipng \
                imagemin-pngquant

# now build all the static assets
RUN npm install --unsafe-perm && \
		node_modules/.bin/gulp build && \
		node_modules/.bin/gulp package && \
		rm -r bower_components node_modules

# set up the config and script we need
COPY lemur.conf.py /www/lemur/lemur.conf.py
RUN mkdir ~/.lemur/ && ln -s /www/lemur/lemur.conf.py ~/.lemur/lemur.conf.py

COPY start.sh /www/lemur/scripts/start.sh
RUN chmod +x /www/lemur/scripts/start.sh

ENV LEMUR_PASSWORD lemur
ENV LEMUR_HOST 0.0.0.0
ENV LEMUR_PORT 8000

EXPOSE $LEMUR_PORT

CMD ["/www/lemur/scripts/start.sh"]