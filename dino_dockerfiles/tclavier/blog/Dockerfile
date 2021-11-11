from tclavier/nginx
run apt-get update \
    && apt-get install -y \
      hugo \
    && apt-get clean

add . /site
run cd /site && /usr/bin/hugo --destination=/var/www
add src/nginx_vhost.conf /etc/nginx/conf.d/blog.conf
