FROM kalilinux/kali-linux-docker
MAINTAINER Christopher Warmbold (warch)

RUN apt-get update && apt-get install -y \
	apache2 \ 
	php \
	set \
	--no-install-recommends \
	&& rm -rf /var/lib/apt/lists/* \
	;apt-get autoremove -y

EXPOSE 80 3000

CMD ["setoolkit"]
