FROM java:8

ADD Hello.java /opt/Hello.java
ADD loop.sh /opt/loop.sh

WORKDIR /opt
RUN javac Hello.java

CMD /opt/loop.sh
