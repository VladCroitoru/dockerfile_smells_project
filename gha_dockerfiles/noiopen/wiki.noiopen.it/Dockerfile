ARG CURRENT_UID=999
FROM mediawiki:1.34.2
ARG CURRENT_UID
RUN useradd -u $CURRENT_UID --home /var/www/data current
ENV APACHE_RUN_USER=current
COPY logo.png /var/www/html/logo.png
