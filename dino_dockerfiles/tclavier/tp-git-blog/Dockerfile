from debian
run apt-get update && apt-get install -y apache2 git && apt-get clean
run apt-get update && apt-get install -y wget && apt-get clean

run wget -O /tmp/hugo.deb -q https://github.com/spf13/hugo/releases/download/v0.15/hugo_0.15_amd64.deb && dpkg -i /tmp/hugo.deb && rm /tmp/hugo.deb

add docker/default.vhost /etc/apache2/sites-available/000-default.conf
run a2enmod dav dav_fs cgi

add docker/start /start
run chmod +x /start
cmd /start

run mkdir /repositories && cd /repositories && git init --bare tp-git.git
add docker/post-receive /repositories/tp-git.git/hooks/post-receive
run chmod +x /repositories/tp-git.git/hooks/post-receive

add . /var/www/
run cd /var/www && hugo --theme=hyde --buildDrafts 
run chown -R www-data:www-data /var/www 
run chown -R www-data:www-data /repositories/

expose 80

