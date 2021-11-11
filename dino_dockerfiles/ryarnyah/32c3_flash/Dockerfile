FROM debian:jessie

RUN apt-get update && \
    apt-get install -y lighttpd python python-dev python-pip wget && \
    pip install pycrypto ipython==5.4.1 && \
    mkdir /src && cd /src && \
    wget https://github.com/ctfs/write-ups-2015/raw/master/32c3-ctf-2015/reversing/flash-300/flash.tgz && \
    tar xzf flash.tgz && \
    cp flash.tgz www/ && \
    mkdir -p /etc/lighttpd/ && \
    mv lighttpd.conf /etc/lighttpd/ && \
    mv bin/md5calc /usr/local/bin/ 

RUN mkdir /home/challenge/ && echo "CTF{$(date +%s | sha256sum | base64)}" > /home/challenge/flag.txt

RUN lighttpd -t -f /etc/lighttpd/lighttpd.conf

VOLUME [ "/tmp", "/var/tmp" ]

USER nobody
WORKDIR src

EXPOSE 8001

ENTRYPOINT ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]
