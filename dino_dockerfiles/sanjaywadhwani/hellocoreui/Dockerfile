# Build from this repo's image
FROM kyma/docker-nginx

# Add src.
COPY . /var/www

#RUN echo "$1" > /var/www/apiserver.txt

WORKDIR /var/www/

RUN pwd
RUN ["chmod", "+x", "./entrypoint.sh"]
#USER hellocoreui-user
ENTRYPOINT ["./entrypoint.sh"]
