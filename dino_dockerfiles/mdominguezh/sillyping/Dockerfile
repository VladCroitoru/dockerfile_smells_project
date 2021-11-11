FROM library/debian:stretch
MAINTAINER manuel.dominguez@gmail.com
RUN apt-get update && \
    apt-get -y upgrade && \
    rm -rf /var/cache/apt /var/lib/dpkg
CMD ["8.8.8.8"]
ENTRYPOINT [ "/bin/ping","-c", "15", "-s" ,"1400", "-i", "0.2" ]
