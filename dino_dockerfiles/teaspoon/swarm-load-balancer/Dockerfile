FROM nginx:latest

RUN apt-get update \
  && apt-get install -y unzip

ADD files/start.sh /bin/start.sh
ADD files/switch /bin/switch
RUN chmod +x /bin/start.sh
RUN chmod +x /bin/switch

ADD files/default.ctmpl /templates/default.ctmpl

ADD https://releases.hashicorp.com/consul-template/0.12.2/consul-template_0.12.2_linux_amd64.zip /usr/bin/
RUN unzip /usr/bin/consul-template_0.12.2_linux_amd64.zip -d /usr/local/bin

ENV LIVE green
ENV BLUE_APP ekaya_vip_blue
ENV GREEN_APP ekaya_vip_green
ENV BLUE_API ekaya_server_blue
ENV GREEN_API ekaya_server_green

EXPOSE 80 8888
ENTRYPOINT ["/bin/start.sh"]
