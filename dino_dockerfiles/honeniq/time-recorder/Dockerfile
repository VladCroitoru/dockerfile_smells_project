FROM node:6-slim
EXPOSE 80

ENV NGINX_VERSION 1.11.1-1~jessie

RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \
	&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get install --no-install-recommends --no-install-suggests -y \
						ca-certificates \
						nginx \
						nginx-module-njs \
	&& rm -rf /var/lib/apt/lists/*

COPY . /opt/time-recorder
WORKDIR /opt/time-recorder

RUN npm install
RUN npm run build

RUN sed -i 's/\/usr\/share\/nginx\/html/\/opt\/time-recorder\/public/g' /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]
