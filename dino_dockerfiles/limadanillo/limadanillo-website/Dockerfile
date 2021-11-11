FROM nginx

RUN  mkdir -p /opt/sites/limadanillo/assets

COPY limadanillo.conf /etc/nginx/conf.d
COPY gzip.conf /etc/nginx/conf.d

COPY . /opt/sites/limadanillo

EXPOSE 80
EXPOSE 443
