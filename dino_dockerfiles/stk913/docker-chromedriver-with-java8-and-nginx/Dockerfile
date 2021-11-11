FROM openjdk:8-jre

ENV NGINX_VERSION 1.10.3-1~jessie
ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN apt-key update && apt-get update
RUN apt-get install apt-transport-https libcurl3-gnutls
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/debian/ jessie nginx" >> /etc/apt/sources.list
RUN echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list

RUN apt-get update && apt-get install --allow-unauthenticated --no-install-recommends --no-install-suggests -y \
	ca-certificates \
	nginx=${NGINX_VERSION} \
	nginx-module-xslt \
	nginx-module-geoip \
	nginx-module-image-filter \
	nginx-module-perl \
	nginx-module-njs \
	gettext-base \
	chromedriver \
	google-chrome-stable \
	xvfb \
	tinywm \
	fonts-ipafont-gothic \
	xfonts-100dpi \
	xfonts-75dpi \
	xfonts-scalable \
	xfonts-cyrillic \
	python \
	x11vnc

RUN apt-get -f install -y
RUN rm -rf /var/lib/apt/lists/*
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log
RUN useradd automation --shell /bin/bash --create-home

ADD ./scripts/ /home/root/scripts
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80 443 8080 5999
CMD ["nginx", "-g", "daemon off;"]
ENTRYPOINT ["sh", "/home/root/scripts/start.sh"]
