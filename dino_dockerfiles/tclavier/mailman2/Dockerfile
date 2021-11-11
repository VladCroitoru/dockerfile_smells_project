from debian
env DEBIAN_FRONTEND noninteractive
run sed -e 's/httpredir.debian.org/debian.mirrors.ovh.net/g' -i /etc/apt/sources.list
run echo "fr_FR.UTF-8 UTF-8" > /etc/locale.gen 

run apt-get update \
    && apt-get install -y \
      apache2 \
      ca-certificates \
      exim4 \
      locales \
      mailman \
      rsync \
    && apt-get clean

run echo "mailman  mailman/default_server_language select fr" | debconf-set-selections \
    && echo "mailman  mailman/site_languages multiselect fr" | debconf-set-selections \
    && echo "mailman  mailman/used_languages string fr" | debconf-set-selections \
    && dpkg-reconfigure mailman

add vhost.conf /etc/apache2/sites-enabled/mailman.conf
#run rm /etc/apache2/sites-enabled/000-default.conf
run a2enmod cgid

add mm_cfg.py /etc/mailman/mm_cfg.py

add update-exim4.conf.conf /etc/exim4/update-exim4.conf.conf
add 04_local_mailman /etc/exim4/conf.d/main/04_local_mailman
add 970_local_mailman /etc/exim4/conf.d/router/970_local_mailman
add 40_local_mailman /etc/exim4/conf.d/transport/40_local_mailman
run mv /var/lib/mailman /mailman

add start /usr/local/bin/start
run chmod +x /usr/local/bin/start
expose 80 25
env MM_PASSWORD=password
cmd ["/usr/local/bin/start"]
