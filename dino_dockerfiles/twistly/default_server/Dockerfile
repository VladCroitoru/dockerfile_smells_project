FROM abiosoft/caddy
ADD index.html /srv/index.html
RUN echo -e '0.0.0.0\nroot /srv\nmarkdown / {\n    ext .html\n    template index.html\n}' > /etc/Caddyfile