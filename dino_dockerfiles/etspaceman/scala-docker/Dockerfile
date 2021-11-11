FROM openjdk:8u151-jdk

MAINTAINER eric.steven.meisel@gmail.com

ENV SCALA_VERSION=2.12.4

#Install Scala
RUN wget "http://www.scala-lang.org/files/archive/scala-${SCALA_VERSION}.tgz" && \
	tar xvf scala-$SCALA_VERSION.tgz && \
	mv scala-$SCALA_VERSION /usr/lib && \
	ln -s /usr/lib/scala-$SCALA_VERSION /usr/lib/scala && \
	echo "export PATH=$PATH:/usr/lib/scala/bin" >> ~/.bashrc && \
	rm scala-$SCALA_VERSION.tgz

#Install SBT
RUN apt-get update && \
	apt-get install apt-transport-https && \
	echo "deb https://dl.bintray.com/sbt/debian /" | tee -a /etc/apt/sources.list.d/sbt.list && \
	apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823 && \
        apt-get update && \
	apt-get install sbt bc
	
CMD ["bash"]
