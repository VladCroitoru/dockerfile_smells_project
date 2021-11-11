FROM python:alpine3.7



RUN mkdir /app && \
	apk add --update git tzdata && \
	pip install -U git+https://github.com/instagrambot/instabot.git@master && \
	pip install -U schedule && \
	git clone https://github.com/instagrambot/instabot --recursive
	
WORKDIR /app

ADD feed.patch .

RUN patch -p0 < feed.patch

EXPOSE 80

VOLUME /app

CMD python
