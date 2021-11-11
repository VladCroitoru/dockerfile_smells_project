FROM dashpay/dashd

USER root

RUN apt-get update && apt-get install -y wget nginx supervisor
RUN sed -i 's/^\(\[supervisord\]\)$/\1\nnodaemon=true/' /etc/supervisor/supervisord.conf

COPY supervisor.conf /etc/supervisor/conf.d/programs.conf
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 443

CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
