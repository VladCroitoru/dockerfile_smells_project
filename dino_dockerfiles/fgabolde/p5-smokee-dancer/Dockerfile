FROM perl:5.18
MAINTAINER Fabrice Gabolde <fabrice.gabolde@gmail.com>

RUN cpanm -n Plack Starman

COPY . /app
WORKDIR /app
RUN cpanm -n --installdeps .

COPY docker-entrypoint-initdb.d /docker-entrypoint-initdb.d
VOLUME /docker-entrypoint-initdb.d
EXPOSE 5000

CMD ["plackup", "-Ilib", "-s", "Starman", "-L", "Delayed", "--port", "5000", "--workers", "2", "bin/app.psgi"]
