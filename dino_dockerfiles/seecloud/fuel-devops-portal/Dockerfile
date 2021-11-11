FROM nginx
MAINTAINER Vitaly Kramskikh <vkramskikh@mirantis.com>

RUN apt-get update && \
    apt-get install --yes curl git-core npm && \
    apt-get remove node && \
    curl -sL https://deb.nodesource.com/setup_6.x | sh && \
    apt-get install -y nodejs

COPY . /app
WORKDIR /app

RUN npm install && npm run build

RUN cp -r /app/dist/* /usr/share/nginx/html && \
    cp /app/etc/nginx/fuel-devops-portal.conf /etc/nginx/conf.d/default.conf
