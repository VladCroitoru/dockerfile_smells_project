#Dockerfile
FROM python:3.5-alpine

#Expose port
EXPOSE 80

#Creating application source directory and expose the volume
RUN mkdir /django_app
VOLUME /django_app

#COPY the build requirements file to the root of image, used during the first init.
COPY requirements.txt /build_requirements.txt

#Install the mandatory packages and some every-day-use packages.
#Leaves only mariadb-client-libs needed for mysqlclient.
RUN apk add --update --no-cache --virtual .build-deps build-base mariadb-dev \
    && pip install -r /build_requirements.txt \
    && apk add --virtual .runtime-deps mariadb-client-libs \
    && apk del .build-deps


# COPY startup script into known file location in container
COPY start.sh /start.sh

# CMD specifies the command to execute to start the server running.
WORKDIR /django_app
CMD ["/start.sh"]
