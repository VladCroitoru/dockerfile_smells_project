FROM ubuntu:16.04
MAINTAINER nenew <http://www.nenew.net>
RUN cp /etc/apt/sources.list /etc/apt/sources.list.backup
RUN sed 's/archive.ubuntu/mirrors.163/g' /etc/apt/sources.list.backup > /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y python-pip
RUN apt-get clean
RUN pip install shadowsocks
ADD /kcptunclient /
ADD /run.sh /
RUN chmod +x /kcptunclient
RUN chmod +x /run.sh
EXPOSE 6606
CMD ["./run.sh"]
