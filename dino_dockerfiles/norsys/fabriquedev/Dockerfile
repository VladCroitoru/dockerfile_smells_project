FROM ubuntu:14.04

# Install Requirements
RUN apt-get update -qq \
    && apt-get install -qy \
        curl

# Install Nginx
RUN apt-get update -qq \
    && apt-get install -qy \
        nginx \
    && sed -i "s|user www-data;|user root;|g" /etc/nginx/nginx.conf \
    && echo "daemon off;" >> /etc/nginx/nginx.conf

# Install Node JS & NPM
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \
    && apt-get update -qq \
    && apt-get install -qy nodejs

# Clean
RUN apt-get -qqy --purge autoremove \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Angular CLI
RUN npm install -g @angular/cli

# Build project
COPY . /src
RUN cd /src \
    && npm install \
    && npm run build --prod

# Configure access with nginx
RUN rm -rf /usr/share/nginx/html \
    && ln -s /src/dist /usr/share/nginx/html

WORKDIR /src
EXPOSE 80

CMD /usr/sbin/nginx -c /etc/nginx/nginx.conf
