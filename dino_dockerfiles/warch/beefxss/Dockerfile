FROM kalilinux/kali-linux-docker
MAINTAINER Christopher Warmbold (warch)

RUN apt-get update && apt-get install -y \
	beef-xss


EXPOSE 3000
CMD beef-xss
