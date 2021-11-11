FROM nginx:1.13.8

MAINTAINER gaku3601

# ツールインストール
RUN apt-get update
RUN apt-get install -y supervisor cron
RUN apt-get install -y letsencrypt
RUN apt-get install -y apache2-utils

# 環境変数設定
ENV TZ=Asia/Tokyo

# supervisorの設定
ADD supervisord.conf /etc/supervisord.conf

# cronの設定(ssl証明書定期更新処理[毎週月曜日AM4:00更新])
ADD ./cron-startup.sh /cron-startup.sh
RUN mkdir /var/log/cron
ADD ./renew.sh /renew.sh
RUN echo '0 4 * * 1 root sh /renew.sh >> /var/log/cron/`date '+\\%Y-\\%m-\\%d'`.log 2>&1' >> /etc/crontab

# nginxの設定
ADD ./default.conf /etc/nginx/conf.d/default.conf
ADD ./default.ssl.conf~ /etc/nginx/conf.d/default.ssl.conf~

# ssl設定
RUN mkdir /usr/share/nginx/html/ssl
RUN chown nginx.nginx /usr/share/nginx/html/ssl
ADD ./start.sh /start.sh

# 起動
CMD /usr/bin/supervisord -c /etc/supervisord.conf
