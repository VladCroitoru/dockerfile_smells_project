FROM maven:3-jdk-8

RUN apt-get install git
RUN git clone https://github.com/EPSI-Coding-Dojo/KataTeube.git
RUN cd KataTeube; \
mvn test
