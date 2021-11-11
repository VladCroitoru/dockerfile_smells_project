FROM node:alpine
MAINTAINER ikasty <mail.ikasty@gmail.com>

WORKDIR /usr/src/app

ADD ./wait-for-it.sh /usr/src/

# get epcis ac
RUN apk add --no-cache --virtual .build git && \
	git clone https://github.com/HaJaehee/jaehee_epcis_ac.git /usr/src/app && \
	apk del .build && \

# settings & install
	sed -i 's/127.0.0.1/ac_api/' conf.json && \
	npm install && \

# for wait-for-it.sh
	chmod 777 /usr/src/wait-for-it.sh && \
	apk --no-cache add bash

CMD /usr/src/wait-for-it.sh -t 0 ac_api:3001 -- npm start