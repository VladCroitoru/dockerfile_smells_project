FROM tdewolff/minify:latest as builder
COPY ./src/html /src/html
RUN cd / && minify --html-keep-conditional-comments --recursive --output . src/; \
sed -i -e "s/{date}/$(date -Iseconds)/g" /src/html/sitemap.xml

FROM nginx:stable-alpine
COPY ./src/nginx.conf /etc/nginx
COPY --from=builder /src/html /srv/html
