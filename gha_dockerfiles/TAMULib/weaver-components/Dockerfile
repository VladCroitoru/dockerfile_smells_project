FROM node:12.14-slim as npm

COPY package.json ./

WORKDIR /app
COPY . .

RUN npm install
RUN npm run build

FROM httpd:2.4-alpine

ARG MAJOR_VERSION=0x
ARG MAJOR_MINOR_VERSION=0.0

COPY --from=npm /app/dist/bundle/ /usr/local/apache2/htdocs/wvr-components/bundle

RUN ln -s /usr/local/apache2/htdocs/wvr-components/bundle /usr/local/apache2/htdocs/wvr-components/latest
RUN ln -s /usr/local/apache2/htdocs/wvr-components/bundle /usr/local/apache2/htdocs/wvr-components/${MAJOR_VERSION}x
RUN ln -s /usr/local/apache2/htdocs/wvr-components/bundle /usr/local/apache2/htdocs/wvr-components/${MAJOR_MINOR_VERSION}

COPY --from=npm /app/src/config-template.json tmp/config-template.json
COPY docker-entrypoint /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint

ENTRYPOINT ["docker-entrypoint"]

RUN apk update; 
RUN apk upgrade;

RUN echo "" >> /usr/local/apache2/conf/httpd.conf
RUN echo "###SPECIFIC CUSTOMIZATIONS###" >> /usr/local/apache2/conf/httpd.conf
RUN echo "" >> /usr/local/apache2/conf/httpd.conf

RUN printf '<Directory /usr/local/apache2/htdocs> \nOrder Allow,Deny \nAllow from all \nAllowOverride all \nHeader set Access-Control-Allow-Origin "*" \n</Directory>' >> /usr/local/apache2/conf/httpd.conf

CMD ["httpd", "-D", "FOREGROUND"]
