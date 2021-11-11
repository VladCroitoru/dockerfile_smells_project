FROM phusion/baseimage:latest
MAINTAINER Ximbesto

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get install -y squid-deb-proxy-client
#RUN apt-get install -y openjdk-6-jre
RUN apt-get install -y default-jre
RUN apt-get install -y unzip
#ADD http://192.168.100.222/forgerock/OpenDJ-2.6.0.zip /
ADD OpenDJ-2.6.0.zip /
RUN useradd -d /var/lib/opendj -m -s /bin/bash opendj
RUN chown opendj:opendj /OpenDJ-2.6.0.zip
RUN su -s /bin/bash opendj -c "unzip /OpenDJ-2.6.0.zip -d /var/lib/"
RUN rm -rf /OpenDJ-2.6.0.zip
ADD opendj.properties /var/lib/opendj/opendj.properties
RUN echo 'foo' > /tmp/foo.txt
RUN cd /var/lib/opendj;./setup  --cli --propertiesFilePath opendj.properties --acceptLicense --no-prompt
RUN echo 'bar' >> /tmp/foo.txt
RUN /usr/sbin/enable_insecure_key
RUN mkdir /etc/service/opendj
ADD opendj.sh /etc/service/opendj/run
RUN chmod +x /etc/service/opendj/run
EXPOSE 389 1686 1689 8080 4444
CMD ["/sbin/my_init"]
#CMD ["./var/lib/opendj/bin/start-ds"]

