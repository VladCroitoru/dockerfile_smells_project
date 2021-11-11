FROM httpd:2.4
COPY ./public-html/ /usr/local/apache2/htdocs

RUN echo "LoadModule rewrite_module modules/mod_rewrite.so" >> /usr/local/apache2/conf/httpd.conf
RUN echo "RewriteEngine on" >> /usr/local/apache2/conf/httpd.conf
RUN echo "RewriteCond %{HTTP:X-Forwarded-Proto} !^$" >> /usr/local/apache2/conf/httpd.conf
RUN echo "RewriteCond %{HTTP:X-Forwarded-Proto} !https [NC]" >> /usr/local/apache2/conf/httpd.conf
RUN echo "RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]" >> /usr/local/apache2/conf/httpd.conf

EXPOSE 80
