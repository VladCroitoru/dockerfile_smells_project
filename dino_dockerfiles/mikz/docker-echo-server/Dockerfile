FROM 3scale/openresty

RUN useradd --system nginx
ADD . /var/www/
RUN ln -sf /var/www/supervisor.conf /etc/supervisor/conf.d/openresty.conf
