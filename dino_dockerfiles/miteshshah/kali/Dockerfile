FROM miteshshah/kalilinux
MAINTAINER Mr.Miteshah@gmail.com

# Install Required Packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y install host whois dnsmap dnsenum thc-ipv6 goofile theharvester lftp telnet w3af nbtscan enum4linux cisco-torch smtp-user-enum amap&& apt-get clean

CMD ["/bin/bash"]
