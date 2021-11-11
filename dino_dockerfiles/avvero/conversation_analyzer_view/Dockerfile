FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && \
    apt-get install git -y && \
    apt-get install software-properties-common -y && \
    apt-get install python-software-properties -y && \
    add-apt-repository ppa:webupd8team/java -y && \
    apt-get update -y
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
RUN apt-get install oracle-java8-installer -y

WORKDIR /tmp

RUN git clone https://github.com/avvero/conversation_analyzer_view.git

WORKDIR conversation_analyzer_view

RUN chmod +x ./gradlew

RUN ./gradlew build

#RUN java -Dserver.port=$PORT -Dspring.profiles.active=def $JAVA_OPTS -jar build/libs/*.war
ENTRYPOINT ["./gradlew"]

EXPOSE 8091