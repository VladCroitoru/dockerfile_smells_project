FROM nginx

RUN apt-get update && apt-get install openssl

COPY entrypoint.sh /root/entrypoint.sh

CMD ["/root/entrypoint.sh"]