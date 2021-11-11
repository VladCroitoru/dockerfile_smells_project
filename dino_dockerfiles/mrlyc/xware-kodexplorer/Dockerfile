FROM w1yd/kodexplorer
MAINTAINER lyc <imyikong@gmail.com>

RUN apt-get update && \
    apt-get install -y libc6-i386 lib32z1 && \
    mkdir -p /data/ && \
    mkdir -p /app/data/User/admin/home/download/ && \
    ln -s /data/TDDOWNLOAD /app/data/User/admin/home/download/TDDOWNLOAD

WORKDIR /xware
ADD Xware1.0.31_x86_32_glibc.tar.gz /xware
ADD monitor.sh /xware

ADD ./app/images/thunder.png /app/static/images/app/thunder.png
ADD ./app/desktop/thunder.oexe /app/data/User/admin/home/desktop/thunder.oexe

VOLUME /app

CMD ["./monitor.sh"]
