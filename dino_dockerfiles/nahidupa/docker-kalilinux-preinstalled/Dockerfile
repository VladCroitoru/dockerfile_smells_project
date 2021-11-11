FROM kalilinux/kali-linux-docker
MAINTAINER nahidul kibria <nahidupa@gmail.com>
#python-httplib2 fimap dependency
#libswitch-perl libssl-dev dotdotpwn dependency

RUN apt-get update\
  && apt-get install --assume-yes nmap netcat\
  sqlmap whatweb wpscan beef fimap dotdotpwn recon-ng\ 
  python-httplib2\  
  libswitch-perl\  
  libssl-dev\
  && apt-get clean
  
#Can't locate LWP/UserAgent.pm in @INC ... dotdotpwn
WORKDIR /tmp
RUN cpan install Bundle::LWP HTTP::Request Net::FTP TFTP Time::HiRes Socket IO::Socket Getopt::Std Switch IO::Socket::SSL

EXPOSE 8000 8001 8002 8003 8004 8005
