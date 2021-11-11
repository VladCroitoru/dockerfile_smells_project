FROM nginx

MAINTAINER David Noyes <david@raspberrypython.com>

COPY index.html /usr/share/nginx/html/index.html
COPY parrot.png /usr/share/nginx/html/parrot.png

CMD /bin/sed -i "s/ffffff/$(cat /dev/urandom | tr -dc 'a-f0-9' | fold -w 6 | head -n 1)/" /usr/share/nginx/html/index.html && nginx -g 'daemon off;'
