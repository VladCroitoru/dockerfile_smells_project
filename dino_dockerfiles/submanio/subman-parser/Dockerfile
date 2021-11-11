FROM submanio/clojure
MAINTAINER Vladimir Iakovlev <nvbn.rm@gmail.com>

RUN lein uberjar

CMD java -jar target/subman-parser-*-SNAPSHOT-standalone.jar
