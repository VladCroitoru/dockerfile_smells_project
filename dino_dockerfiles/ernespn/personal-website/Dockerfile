# This image will be based on the official nodejs docker image
FROM node:argon

#Install NGINX
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \
	&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get install --no-install-recommends --no-install-suggests -y \
						ca-certificates \
						nginx \
						nginx-module-xslt \
						nginx-module-geoip \
						nginx-module-image-filter \
						nginx-module-perl \
						nginx-module-njs \
						gettext-base \
	&& rm -rf /var/lib/apt/lists/*
#RUN apt-get install git-core

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log


# APP BUILD
# Set in what directory commands will run
WORKDIR /home/app
# Put all our code inside that directory that lives in the container
ADD     . /home/app
# Install Bower & Grunt
RUN     npm cache clean --silent
RUN     npm install -g bower grunt-cli grunt-init --silent
#Install dependencies
RUN     npm install --silent
# RUN     git config --global url."https://".insteadOf git://
RUN     bower cache clean --allow-root
RUN     GIT_DIR=/tmp bower install --allow-root --silent
#RUN     bower install --allow-root
# Build 
RUN     GIT_DIR=/tmp grunt build
# Copy to NGINX
RUN     cp -ar dist/* /usr/share/nginx/html/
RUN		cp default.conf /etc/nginx/conf.d/

#Running NGINX
EXPOSE 9000
CMD ["nginx", "-g", "daemon off;"]
