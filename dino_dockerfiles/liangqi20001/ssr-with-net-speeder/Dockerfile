# ssr-with-net-speeder

FROM centos:7.3.1611

RUN yum install python python-pip python-m2crypto libnet1-dev libpcap0.8-dev libnet libpcap libnet-devel libpcap-devel git gcc -y
RUN git clone https://github.com/snooda/net-speeder.git net-speeder
RUN git clone -b manyuser https://github.com/breakwa11/shadowsocks.git ssr
WORKDIR net-speeder
RUN chmod +x build.sh
RUN ./build.sh

RUN mv net_speeder /usr/local/bin/
RUN chmod +x /usr/local/bin/net_speeder

RUN nohup /usr/local/bin/net_speeder venet0 "ip" >/dev/null 2>&1 &
RUN ping www.baidu.com -c 5

WORKDIR /ssr/shadowsocks
RUN python server.py -p 1443 -k password -m aes-256-cfb -O auth_sha1_v4 -o http_simple -d start
