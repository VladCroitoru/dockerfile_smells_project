FROM kalilinux/kali-linux-docker
MAINTAINER info@feltsecure.com

   
RUN echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" > /etc/apt/sources.list && \
echo "deb-src http://http.kali.org/kali kali-rolling main contrib non-free" >> /etc/apt/sources.list
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update && apt-get install -y \
    kali-linux-top10 \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get dist-upgrade && apt-get clean

CMD ["/bin/bash"]
