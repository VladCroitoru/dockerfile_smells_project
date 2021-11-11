FROM linuxconfig/lemp

RUN apt-get update && apt-get install -y git

WORKDIR /var/www/html

RUN git clone https://tt-rss.org/gitlab/fox/tt-rss.git 

RUN chmod 777 -R ./tt-rss/



EXPOSE 80 3306
CMD ["supervisord"]
