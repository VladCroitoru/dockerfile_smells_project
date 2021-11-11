#既存のプロジェクトのrubyのバージョンを指定
FROM ruby:2.6.3
#dockerizeパッケージダウンロード用環境変数
#ENV DOCKERIZE_VERSION v0.6.1

#パッケージの取得
RUN apt-get update && \
	apt-get install -y --no-install-recommends\
	#build-essential  \
	wget \
	git \
	vim \
	#&& wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
	#&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
	#&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* \
	&& git clone -b stable --depth 1 https://github.com/shirasagi/shirasagi /var/www/shirasagi

WORKDIR /var/www/shirasagi

COPY /config config

RUN bundle install --without development test \
	mkdir tmp/sockets
