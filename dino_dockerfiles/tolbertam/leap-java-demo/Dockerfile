FROM openjdk:latest
RUN apt-get update
RUN apt-get install -y build-essential ntp
ADD leap-a-day.c /
RUN gcc -lrt leap-a-day.c -o leap-a-day
ADD LeapTest.java /
RUN javac /LeapTest.java
ADD leap_demo.sh /
ENTRYPOINT ["/leap_demo.sh"]

