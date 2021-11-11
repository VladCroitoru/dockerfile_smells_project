FROM kalilinux/kali-linux-docker
MAINTAINER diguo@foxmail.com

RUN apt-get update && apt-get install -y ssh metasploit-framework
RUN service ssh start; service postgresql start && msfdb init

EXPOSE 22

CMD ["/bin/bash"]
