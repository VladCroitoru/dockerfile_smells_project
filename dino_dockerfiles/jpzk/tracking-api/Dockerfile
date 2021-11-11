FROM java:8 

RUN apt-get install -y -f git wget unzip 
RUN mkdir /var/data
RUN mkdir /var/data/agg

WORKDIR /
ADD target/scala-2.10/tracking-api.jar /
ADD application.conf /
ADD docker/tracking-api/start.sh /
RUN chmod +x /start.sh

EXPOSE 9990
EXPOSE 8888

WORKDIR /
ENTRYPOINT ["/bin/bash","/start.sh"]

