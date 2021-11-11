FROM ecompositor/centos-scala:latest

#MAINTAINER michael klatskin <michael@ecompositor.com>
#Most work done by Michael Klatskin
MAINTAINER Matt Koski <maccam912@gmail.com>

WORKDIR /opt/titan-0.5.4-hadoop2

RUN curl -o /opt/titan.zip http://s3.thinkaurelius.com/downloads/titan/titan-0.5.4-hadoop2.zip

RUN unzip /opt/titan.zip -d /opt/ && \
    rm /opt/titan.zip

ADD rexster-titan.xml.template /opt/titan-0.5.4-hadoop2/
ADD run.sh /opt/titan-0.5.4-hadoop2/
RUN chmod +x run.sh

EXPOSE 8182
EXPOSE 8183
EXPOSE 8184
EXPOSE 9160
CMD ["/bin/sh", "-e", "/opt/titan-0.5.4-hadoop2/run.sh"]
