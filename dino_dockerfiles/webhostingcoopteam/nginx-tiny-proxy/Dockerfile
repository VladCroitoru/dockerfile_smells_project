FROM nginx:alpine

ENV WHC_NGINX 20200204

RUN apk update && \
apk upgrade && \
apk add openssl && \
rm -rf /var/cache/apk/*

# removing bash
#apk add bash && \

COPY nginx /assets
CMD ["/assets/start.sh"]
