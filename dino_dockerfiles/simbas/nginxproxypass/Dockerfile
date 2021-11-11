FROM nginx:1.11.8

ENV PROXY_PASS=$PROXY_PASS

COPY default.conf.template /etc/nginx/conf.d/default.conf.template
COPY start.sh ./start.sh

ENTRYPOINT [ "./start.sh" ]