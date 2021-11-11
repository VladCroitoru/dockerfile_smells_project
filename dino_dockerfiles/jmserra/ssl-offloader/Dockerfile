FROM nginx:alpine

COPY nginx.tpl /etc/nginx/nginx.tpl
RUN rm /etc/nginx/nginx.conf

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 443
