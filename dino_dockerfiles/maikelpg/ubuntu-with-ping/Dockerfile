FROM ubuntu

RUN apt-get update
RUN apt-get install apt-utils -y
RUN apt-get install iputils-ping -y

CMD ["ping", "-c 4", "8.8.8.8"]
