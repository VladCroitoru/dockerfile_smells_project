FROM nginx
MAINTAINER Lukas Loesche <lloesche@fedoraproject.org>

COPY auth-proxy.template /etc/nginx/conf.d/
COPY htpasswd.template /etc/nginx/auth/htpasswd.template
COPY startup /startup
RUN rm -f /etc/nginx/conf.d/default.conf && \
    chmod +x /run

EXPOSE 80 443

CMD ["/startup"]
