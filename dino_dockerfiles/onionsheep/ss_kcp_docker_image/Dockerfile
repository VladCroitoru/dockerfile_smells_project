FROM fedora:latest
MAINTAINER Liu Cong <onion_sheep@163.com>

COPY ./res/shadowsocks-server /opt/shadowsocks-server
COPY ./res/kcptun-server /opt/kcptun-server
COPY ./run.sh /root/run.sh
COPY ./webui /root/webui
COPY ./res/init.sh /root/init.sh

RUN bash -x /root/init.sh
# install nginx
# RUN dnf install -y nginx

# echo machine app.arukas.io > /root/.netrc
# echo "    login #{ARUKAS_JSON_API_TOKEN}" >> /root/.netrc
# echo "    password #{ARUKAS_JSON_API_SECRET}" >> /root/.netrc

EXPOSE 8888
EXPOSE 22
EXPOSE 4000
EXPOSE 4001
EXPOSE 4002

CMD ["/root/run.sh"]
