FROM ubuntu
RUN apt-get update
RUN apt-get install -y python
ENV SSPWD abcd1234
ENV SSPORT 12345
ADD ./shadowsocks.sh /var/
WORKDIR /var/
RUN chmod +x shadowsocks.sh
RUN /var/shadowsocks.sh
EXPOSE 12345:12345



