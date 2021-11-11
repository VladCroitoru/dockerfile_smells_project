FROM linuxserver/nginx

# install packages
RUN apk add php7-sqlite3

# install TwoFactorAuth
RUN git clone -b master --single-branch https://github.com/Arno0x/TwoFactorAuth.git /config/www/twofactorauth

VOLUME /config

EXPOSE 443
