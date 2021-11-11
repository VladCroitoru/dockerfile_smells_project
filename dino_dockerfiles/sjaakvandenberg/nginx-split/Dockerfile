FROM ubuntu

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y \
  nginx

ADD ./nginx.conf /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default
ADD ./sites-enabled/ /etc/nginx/sites-enabled

ADD app/ /app

EXPOSE 80

WORKDIR /app

CMD ["nginx", "-g", "daemon off;"]
