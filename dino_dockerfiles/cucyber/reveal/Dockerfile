FROM        alpine

RUN         addgroup -S cucyber && adduser -S -h /var/lib/reveal-multiplex -s /sbin/nologin -DH -G cucyber cucyber

RUN         apk --update add nodejs-npm setpriv

COPY        ext /ext
COPY        reveal-multiplex /ext/lib/reveal-multiplex

RUN         cd /ext/lib/reveal-multiplex; npm install

CMD         /ext/bin/cucyber-init

EXPOSE      1948
