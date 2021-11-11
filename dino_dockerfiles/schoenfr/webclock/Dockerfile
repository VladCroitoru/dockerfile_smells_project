FROM java

MAINTAINER René Schönfelder <schoenfelder2211@gmail.com>

COPY . /prj

RUN echo "deb http://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list
RUN apt-key update
RUN apt-get update
RUN apt-get -y --force-yes install sbt

WORKDIR /prj

RUN sbt assembly

COPY target/scala-2.11/webclock-assembly-1.0.jar /app/webclock.jar

USER daemon

WORKDIR /app

ENTRYPOINT java -jar webclock.jar

EXPOSE 8080
