FROM alpine:3.13

# install
RUN apk --update add apache2 \
 && rm -f /var/cache/apk/* 

# configure
RUN mkdir -p /run/apache2 \
 && ln -s /dev/stderr /var/log/apache2/error.log \
 && ln -s /dev/stdout /var/log/apache2/access.log \
 && mkdir -p /var/www/sample-content

# download tears of steel
RUN cd /var/www/sample-content \
 && wget https://usp-s3-storage.s3.eu-central-1.amazonaws.com/tears-of-steel-remix-demo.zip \
 && unzip tears-of-steel-remix-demo.zip -d /var/www/sample-content/ \
 && rm -rf tears-of-steel-remix-demo.zip


COPY sample-content.conf.in /etc/apache2/conf.d/sample-content.conf.in
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

# copy logo video
COPY content/remix08_400k.mp4 /var/www/sample-content/remix08_400k.mp4
COPY content/remix08_800k.mp4 /var/www/sample-content/remix08_800k.mp4
COPY content/remix08_1200k.mp4 /var/www/sample-content/remix08_1200k.mp4
COPY content/remix08_2000k.mp4 /var/www/sample-content/remix08_2000k.mp4
COPY content/remix08_3000k.mp4 /var/www/sample-content/remix08_3000k.mp4
COPY content/remix08_audio.mp4 /var/www/sample-content/remix08_audio.mp4
COPY content/remix08_dref.mp4 /var/www/sample-content/remix08_dref.mp4

RUN chmod +x /usr/local/bin/entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["httpd", "-DFOREGROUND"]
