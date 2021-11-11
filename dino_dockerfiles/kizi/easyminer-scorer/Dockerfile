FROM java:8

MAINTAINER Jaroslav Kuchar - https://github.com/jaroslav-kuchar

RUN apt-get update && apt-get install -y \
	git \
	maven

RUN update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-8-openjdk-amd64/bin/java 1
RUN update-alternatives --set java /usr/lib/jvm/java-8-openjdk-amd64/bin/java

RUN git clone https://github.com/KIZI/EasyMiner-Scorer.git
WORKDIR EasyMiner-Scorer
RUN mvn clean package -DskipTests
EXPOSE 8080
ENTRYPOINT ["java","-jar","target/easyminer-scorer.war"]