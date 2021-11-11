FROM nginx:mainline-alpine
 
RUN apk add --no-cache --update git && rm -rf /var/cache/apk/*;
RUN rm -rf /usr/share/nginx/html/ && \
    git clone https://github.com/glowing-bear/glowing-bear.git /usr/share/nginx/html/;
CMD git -C /usr/share/nginx/html/ pull && nginx -g "daemon off;"
