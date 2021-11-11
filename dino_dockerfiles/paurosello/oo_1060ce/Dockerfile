FROM    paurosello/oo_1060:v2

EXPOSE 8080
EXPOSE 8443

RUN apt-get update && apt-get install -y --allow-unauthenticated \
  unzip \
  wget \
  bzip2

RUN ./root/community-installer-linux64.bin -s /root/silent.properties
CMD /usr/local/hp/oo/central/bin/central start && tail -f /dev/null
