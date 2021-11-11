FROM catatnight/postfix

ADD installblackhole.sh /opt/

ENV maildomain=mail.blackhole.local
ENV smtp_user=blackhole:blackhole

CMD /opt/install.sh;/opt/installblackhole.sh;/usr/bin/supervisord -c /etc/supervisor/supervisord.conf
