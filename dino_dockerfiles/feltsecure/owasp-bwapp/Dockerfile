FROM tutum/lamp:latest

ENV DEBIAN_FRONTEND noninteractive

# Preparation
RUN rm -fr /app/* && \
  apt-get update && apt-get install -yqq wget unzip php5-curl dnsutils && \
  rm -rf /var/lib/apt/lists/*

# Deploy bWAPP
RUN wget -O /tmp/bwapp.zip https://sourceforge.net/projects/bwapp/files/latest/download && \
  unzip /tmp/bwapp.zip -d /tmp/bwapp && \
  mv /tmp/bwapp/bWAPP/* /app && \
  rm -rf /tmp/bwapp*

# Setup
RUN sed -i 's/db_password = "bug"/db_password = ""/g' /app/admin/settings.php

EXPOSE 80 3306
CMD ["/run.sh"]

