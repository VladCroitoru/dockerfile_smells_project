FROM python:alpine

ARG VERSION=master

RUN \
    apk add --no-cache unzip wget ca-certificates gcc openldap-dev binutils-libs binutils gmp isl libgomp libatomic libgcc pkgconf pkgconfig mpfr3 mpc1 libstdc++ libc-dev musl-dev mariadb-dev postgresql-dev nginx gettext jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev

RUN \
    cd /var/www; \
    wget -q -O ideax.tar.gz https://github.com/filhocf/ideax/archive/master.tar.gz; \
    tar xf ideax.tar.gz; \
    mv ideax-master ideax; \
    rm ideax.tar.gz; \
    cd ideax; \
    pip install -r docker/requeriments.txt

#RUN \
#    apk del binutils-libs binutils gmp isl libgomp libatomic libgcc pkgconf pkgconfig mpfr3 mpc1 libstdc++ gcc musl-dev libc-dev zlib-dev openssl-dev mariadb-common mariadb-client-libs libaio mariadb-libs mariadb-dev db libsasl cyrus-sasl-dev libuuid libblkid libfdisk libmount libsmartcols util-linux-dev unzip wget

WORKDIR /var/www/ideax

COPY ./docker/entrypoint.sh /
COPY ./docker/initialdata.json /var/www/ideax
COPY ./docker/nginx.conf /etc/nginx/

CMD ["/entrypoint.sh"]
