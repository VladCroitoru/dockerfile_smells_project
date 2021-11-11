
FROM ubuntu:14.04
MAINTAINER Henry Hoang "henry.hoang@j2.com"

RUN apt-get -y update && apt-get -yq install default-jdk
#RUN javac ConvertMoneyToDollarBills.java
#RUN java ConvertMoneyToDollarBills


EXPOSE 80

ADD . /
#CMD ["./run.sh"]

ENTRYPOINT ["./run.sh"]



