FROM elasticsearch:2.3.3
MAINTAINER fghpdf "quxiangxuan@shimo.im"
ENV REFRESHED_AT 2017-08-01
RUN curl -O -# https://dn-shimo-attachment.qbox.me/9rNI7ufNwcQYOgrd/plugins.zip
RUN unzip -o -d /usr/share/elasticsearch/plugins plugins.zip
RUN /usr/share/elasticsearch/bin/plugin install delete-by-query 
EXPOSE 9200 9300
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["elasticsearch"]
