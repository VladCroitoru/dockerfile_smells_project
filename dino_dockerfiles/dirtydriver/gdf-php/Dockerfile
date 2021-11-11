FROM nimmis/apache-php5
RUN apt-get update
RUN apt-get install git -y
RUN apt-get install php5-mysql -y
RUN cd /var/www/html && rm index.html && git clone https://github.com/dirtydriver/gdf-php.git  && mv gdf-php/*php .

EXPOSE 80
WORKDIR /var/www/html