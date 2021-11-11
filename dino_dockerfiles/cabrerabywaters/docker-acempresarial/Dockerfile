FROM cabrerabywaters/nginx-laravel
RUN git clone https://github.com/cabrerabywaters/acempresaral.git /usr/share/nginx/app2
RUN rm -rf  /usr/share/nginx/app
RUN mv /usr/share/nginx/app2 /usr/share/nginx/app

COPY build/.env /usr/share/nginx/app
RUN chown -R www-data.www-data /usr/share/nginx/app
RUN chown -R www-data.www-data /usr/share/nginx/
RUN chmod -R 755 /usr/share/nginx/app
RUN chmod -R 777 /usr/share/nginx/app/storage

RUN cd /usr/share/nginx/app && composer install 
RUN cd /usr/share/nginx/app && npm install 

