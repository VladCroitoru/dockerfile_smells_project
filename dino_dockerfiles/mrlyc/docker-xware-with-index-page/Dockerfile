FROM zwh8800/xware

WORKDIR /xware

ADD site.conf ./site.conf
ADD entry.sh ./entry.sh

RUN apt-get update && \
    apt-get install -y nginx && \
    cat ./site.conf > /etc/nginx/sites-available/default && \
    systemctl enable nginx

EXPOSE 80

ENV FILE_EXPIRES 43200

ENTRYPOINT ["./entry.sh"]
