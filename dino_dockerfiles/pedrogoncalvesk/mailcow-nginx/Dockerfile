FROM nginx:mainline-alpine

LABEL maintainer "Pedro Pereira <pedrogoncalvesp.95@gmail.com>"

COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod +x /docker-entrypoint.sh

COPY conf /etc/nginx/conf.d

EXPOSE 80 443

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["nginx", "-g", "daemon off;"]
