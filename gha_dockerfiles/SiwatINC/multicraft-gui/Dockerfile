FROM ghcr.io/siwatinc/nginx-pagespeed
RUN wget https://www.multicraft.org/download/linux64 && tar -xvzf ./linux64 && rm ./linux64 && cp -rv ./multicraft/panel / && rm -rv ./multicraft && rm -rv /initializer/initialize-builtin.sh
COPY ./initialize-builtin.sh /initializer/initialize-builtin.sh
CMD chmod +x /initializer/initialize-builtin.sh && /initializer/initialize-builtin.sh && service php7.3-fpm start && nginx
