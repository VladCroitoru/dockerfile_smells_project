FROM nginx:stable

LABEL maintainer="Rainist <engineering@rainist.com>"

COPY run.sh .
COPY nginx.conf /etc/nginx/conf.d/default.conf

ENTRYPOINT ["./run.sh"]
