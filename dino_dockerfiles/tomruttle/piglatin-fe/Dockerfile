FROM tomruttle/apache
MAINTAINER Tom Ruttle <tom@tomruttle.com>

COPY . /app

# Configure /app folder
RUN chown root:www-data /app -R &&\
    cd /app && find . -type d -exec chmod u=rx,g=rx,o= '{}' \; &&\
    cd /app && find . -type f -exec chmod u=r,g=r,o= '{}' \; &&\
    rm -fr /var/www && ln -s /app /var/www

# These are unnecessary, as they are specified in the base image
# but they make it clearer what's going on.
EXPOSE 80
ENTRYPOINT ["/usr/sbin/apache2"]
CMD ["-D", "FOREGROUND", "-k", "start"]
