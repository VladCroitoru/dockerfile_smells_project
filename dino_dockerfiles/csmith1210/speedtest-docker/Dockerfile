FROM phusion/baseimage

RUN apt-get update && apt-get install -y g++ cmake make libcurl4-openssl-dev libxml2-dev libssl-dev

RUN mkdir -p /tmp/build /tmp/src
RUN cd /tmp/src && \
    curl -L https://github.com/csmith1210/SpeedTest/archive/master.tar.gz | tar xz --strip=1 && \
    cd /tmp/build && cmake -DCMAKE_BUILD_TYPE=Release ../src && make install && \
    apt-get remove --purge -y gcc make cmake libcurl4-openssl-dev libxml2-dev libssl-dev && \
    apt-get install -y libxml2 libcurl3 && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/build /tmp/src

ADD run.sh /home/
RUN chmod +x /home/run.sh

ENTRYPOINT ["/home/run.sh"]
