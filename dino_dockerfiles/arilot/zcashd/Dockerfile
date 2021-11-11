FROM debian:9.2

ENV PATH "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -yq wget supervisor nginx gnupg

RUN sed -i 's/^\(\[supervisord\]\)$/\1\nnodaemon=true/' /etc/supervisor/supervisord.conf

RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends apt-transport-https ca-certificates wget && \
  wget -qO - https://apt.z.cash/zcash.asc | apt-key add - && \
  echo "deb https://apt.z.cash/ jessie main" | tee /etc/apt/sources.list.d/zcash.list && \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends zcash && \
  apt-get autoclean && \
  mkdir -p /root/.zcash-params /root/.zcash

RUN zcash-fetch-params

ADD supervisord.conf /etc/supervisor/conf.d/programs.conf
ADD nginx.conf /etc/nginx/nginx.conf

EXPOSE 443

CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
