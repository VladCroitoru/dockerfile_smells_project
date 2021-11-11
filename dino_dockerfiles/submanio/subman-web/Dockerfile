FROM submanio/clojure
MAINTAINER Vladimir Iakovlev <nvbn.rm@gmail.com>

USER root
RUN apt-get install software-properties-common python-software-properties -yqq --no-install-recommends
RUN add-apt-repository ppa:chris-lea/node.js  -y
RUN apt-get update -yqq
RUN apt-get install nodejs ruby -yqq --no-install-recommends
RUN npm install -g bower
RUN gem install sass
USER clojure

RUN lein bower install
RUN sass resources/public/main.sass > resources/public/main.css

RUN lein cljx once
RUN lein with-profile uberjar cljsbuild once >> /dev/null 2>> /dev/null
RUN lein ring uberjar

CMD java -jar target/subman-web-*-SNAPSHOT-standalone.jar
