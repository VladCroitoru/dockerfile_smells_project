FROM okdocker/nginx:mainline

# Default values
ENV TIMEZONE=Europe/Moscow
ENV LETSENCRYPT=false
ENV LE_EMAIL=some@mail
ENV LE_DNAME=www.error.host
ENV LE_RT=1y

ADD script/*.sh /

RUN \
    chmod +x /entrypoint.sh && \
    apt-get update &&\
    apt-get install -y certbot tzdata openssl

EXPOSE 80
EXPOSE 443

CMD ["/entrypoint.sh"]
#EOF#