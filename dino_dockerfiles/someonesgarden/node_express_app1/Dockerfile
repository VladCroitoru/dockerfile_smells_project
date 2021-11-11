FROM someonesgarden/node_express_base:latest

MAINTAINER 0.1 Daisuke Nishimura d@someonesgarden.org

#RUN bower install angular angular-material \
#angular-messages angular-route \
#angular-resource angular-sanitize \
#angular-local-storage --save

RUN apt-get update -y && \
apt-get install rhino -y

#RUN npm install java -y

RUN bower install d3 --save

RUN npm install \
# HTMLファイルの解析用
cheerio cheerio-httpcli \
# XMLの解析用
xml2js \
# ダウンロード処理に利用
request

# phantomJSとcaspterJSをnpmでinstallする場合（動作確認済み）
# install phantomJS + caspterJS
# phantom > 2ではcoffeescriptに非対応のためバージョンを下げてインストール
RUN npm install -g phantomjs@1.9.17 casperjs@1.1.0-beta3

# phantomJSとcaspterJSをソースからinstallする場合（動作確認済み）
#ENV PHANTOMJS_VERSION 1.9.7
#RUN mkdir -p /srv/var && \
#  wget -q --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \
#  tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \
#  rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \
#  mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /srv/var/phantomjs && \
#  ln -s /srv/var/phantomjs/bin/phantomjs /usr/bin/phantomjs && \
#  git clone https://github.com/n1k0/casperjs.git /srv/var/casperjs && \
#  ln -s /srv/var/casperjs/bin/casperjs /usr/bin/casperjs && \
#  apt-get autoremove -y && \
#  apt-get clean all
####

COPY download.coffee /usr/src/app/download.coffee
COPY funcs.coffee /usr/src/app/funcs.coffee
COPY app.coffee /usr/src/app/app.coffee


COPY routes /usr/src/app/routes/
COPY public /usr/src/app/public/
COPY views /usr/src/app/views/
COPY bin /usr/src/app/bin/


WORKDIR /usr/src/app

EXPOSE 8080

CMD [ "coffee", "bin/www.coffee" ]
#CMD ["phantomjs", "-v"]



