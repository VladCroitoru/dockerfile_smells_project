FROM nginx

RUN apt-get update \
  && apt-get install -y\
    apt-transport-https \
    build-essential \
    bzip2 \
    curl \
    git \
    rlwrap \
    vim \
  && curl -sL https://deb.nodesource.com/setup_7.x | bash - \
  && apt-get install --assume-yes --no-install-recommends nodejs \
  && apt-get clean

RUN mkdir -p /usr/share/nginx/html

ADD ./package.json /usr/share/nginx/html

WORKDIR /usr/share/nginx/html

RUN npm install

ADD . /usr/share/nginx/html

COPY ./nginx.conf /etc/nginx/nginx.conf

RUN npm run build

CMD nginx -g 'daemon off;'
