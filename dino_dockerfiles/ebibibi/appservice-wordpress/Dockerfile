FROM wordpress
LABEL maintainer "Masahiko Ebisuda<ebibibi@gmail.com>"

# ------------------------
# SSH Server support
# ------------------------
RUN apt-get update \
    && apt-get install -y --no-install-recommends openssh-server \
    && echo "root:Docker!" | chpasswd

COPY sshd_config /etc/ssh/

EXPOSE 2222 80 443

#--------------------------
# Install wordpress plugins
#--------------------------
# これから使う`wget`と`unzip`を入れる
RUN apt-get update
RUN apt-get -y --force-yes -o Dpkg::Options::="--force-confdef" install wget unzip

# プラグインファイルの一時ダウンロード先
WORKDIR /tmp/wp-plugins

# プラグインファイルをダウンロード
RUN wget https://downloads.wordpress.org/plugin/akismet.4.1.12.zip
RUN wget https://downloads.wordpress.org/plugin/drift.zip
RUN wget https://downloads.wordpress.org/plugin/google-sitemap-generator.4.1.1.zip
RUN wget https://downloads.wordpress.org/plugin/jetpack.10.1.zip
RUN wget https://downloads.wordpress.org/plugin/pixabay-images.zip
RUN wget https://downloads.wordpress.org/plugin/really-simple-ssl.5.1.0.zip
RUN wget https://downloads.wordpress.org/plugin/wordfence.7.5.5.zip
RUN wget https://downloads.wordpress.org/plugin/wp-azure-offload.2.0.zip
RUN wget https://downloads.wordpress.org/plugin/wp-multibyte-patch.2.9.zip
RUN wget https://downloads.wordpress.org/plugin/edump.zip
RUN wget https://downloads.wordpress.org/plugin/feedzy-rss-feeds.zip



# プラグインをWordPressのプラグインディレクトリに解凍する
RUN unzip -o './*.zip' -d /usr/src/wordpress/wp-content/plugins
RUN chown -R www-data:www-data /usr/src/wordpress/wp-content

# 一時ダウンロード先内の全ファイルの削除
RUN rm -rf '/tmp/wp-plugins'

# 戻る
WORKDIR /var/www/html

#------------------------
# Install Wordpress theme
#------------------------

# テーマファイルの一時ダウンロード先
WORKDIR /tmp/wp-themes

# テーマファイルをダウンロード
RUN wget https://github.com/ebibibi/wordpress-cocoon/raw/master/Themes/cocoon-child-master-1.1.3.zip
RUN wget https://github.com/ebibibi/wordpress-cocoon/raw/master/Themes/cocoon-master-2.3.5.1.zip
# get latest theme from https://wp-cocoon.com/downloads/


# テーマをWordPressのテーマディレクトリに解凍する
RUN unzip './*.zip' -d /usr/src/wordpress/wp-content/themes
RUN chown -R www-data:www-data /usr/src/wordpress/wp-content

# 一時ダウンロード先内の全ファイルの削除
RUN rm -rf '/tmp/wp-themes'

# 戻る
WORKDIR /var/www/html


#------------------------
# Create php.ini
#------------------------
#COPY php.ini /usr/local/etc/php/conf.d/php.ini

# 戻る
WORKDIR /var/www/html


#--------------------------
# Install emacs
#--------------------------
#RUN apt-get -y --force-yes -o Dpkg::Options::="--force-confdef" install emacs

#------------------------
# 実行
#------------------------
COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh 
ENTRYPOINT ["/entrypoint.sh"]
CMD ["apache2-foreground"]