FROM node:carbon as build
COPY . /src
RUN cd /src && npm install && npm run build

FROM httpd:2.4 as production
COPY --from=build /src/httpd.conf /usr/local/apache2/conf/httpd.conf
COPY --from=build /src/dist/ /usr/local/apache2/htdocs/