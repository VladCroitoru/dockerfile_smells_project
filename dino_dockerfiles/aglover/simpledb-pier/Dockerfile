FROM aglover/java8-pier
MAINTAINER Andy Glover "ajglover@gmail.com"

RUN apt-get update -y

# see https://github.com/stephenh/fakesdb -- issue 13 https://github.com/stephenh/fakesdb/issues/13
RUN wget http://repo.joist.ws/com/bizo/fakesdb-standalone_2.9.1/2.6.1/fakesdb-standalone_2.9.1-2.6.1.jar -O fakesdb-standalone.jar
RUN mkdir local-sdb
RUN mv fakesdb-standalone.jar local-sdb/. && cd local-sdb && jar xf fakesdb-standalone.jar
RUN cd local-sdb && rm fakesdb-standalone.jar
RUN cd local-sdb && jar cmf manifest.mf fakesdb-standalone.jar .


EXPOSE 8080

CMD ["java", "-jar", "local-sdb/fakesdb-standalone.jar"]
