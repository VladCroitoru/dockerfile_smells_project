FROM dockerfile/java:latest

#MAINTAINER Abhinav Pobbati <apobbati@codeblock.io>
MAINTAINER Matt Koski <maccam912@gmail.com>

WORKDIR /opt/titan-0.5.3-hadoop2

RUN curl -o /opt/titan.zip http://s3.thinkaurelius.com/downloads/titan/titan-0.5.3-hadoop2.zip

RUN unzip /opt/titan.zip -d /opt/ &&\
    rm /opt/titan.zip

ADD rexster-titan.xml.template /opt/titan-0.5.3-hadoop2/
ADD run.sh /opt/titan-0.5.3-hadoop2/

EXPOSE 8182:8182
EXPOSE 8183:8183
EXPOSE 8184:8184

RUN chmod +x /opt/titan-0.5.3-hadoop2/run.sh

CMD ["/bin/sh", "-e", "/opt/titan/run.sh"]
