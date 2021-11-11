FROM logstash:5.4

MAINTAINER Manuel García-Amado
RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip 

ADD . /usr/src/app
WORKDIR /usr/src/app
RUN pip3 install -r requirements.txt
RUN python3 /usr/src/app/setup.py install
RUN logstash-plugin install logstash-output-elasticsearch logstash-input-beats 
CMD ["logstash",  "-f", "logstash-collector.conf"]
