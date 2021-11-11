FROM python:3.6-stretch

WORKDIR /root

RUN apt-get update && apt-get install -y gnupg1 apt-transport-https ca-certificates \
    && wget -O nginx_signing.key https://nginx.org/keys/nginx_signing.key \
    && apt-key add nginx_signing.key \
    && rm nginx_signing.key \
    && echo "deb http://nginx.org/packages/mainline/debian/ stretch nginx" >> /etc/apt/sources.list \
    && echo "deb-src http://nginx.org/packages/mainline/debian/ stretch nginx" >> /etc/apt/sources.list \
    && wget -O pubkey.gpg https://dl.yarnpkg.com/debian/pubkey.gpg \
    && apt-key add pubkey.gpg \
    && rm pubkey.gpg \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" >> /etc/apt/sources.list \
    && wget -O setup_8.x.sh https://deb.nodesource.com/setup_8.x \
    && bash setup_8.x.sh \
    && apt-get install -y nginx nodejs yarn \
    && rm setup_8.x.sh

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN cd frontend && yarn install && yarn run build && cp ../nginx.conf /etc/nginx/nginx.conf

CMD ["bash", "start.sh"]