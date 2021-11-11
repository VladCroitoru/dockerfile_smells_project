FROM nginx:stable
RUN curl --silent --location https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y \
  nodejs
RUN echo "Node: " && node -v
RUN echo "NPM: " && npm -v
COPY . /usr/share/nginx/html
WORKDIR /usr/share/nginx/html
RUN npm i && npm run build
COPY docker/default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
