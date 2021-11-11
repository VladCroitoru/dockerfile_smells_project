FROM java

ENV HELLO  kin
WORKDIR /home/root/myjava
COPY Hello.java src/Hello.java
RUN mkdir bin

RUN javac -d bin src/Hello.java

ENV KIN_HOME=/home/root/kin

VOLUME ["myvo"]


ENTRYPOINT ["java", "-cp", "bin", "Hello"]
