FROM httpd
MAINTAINER exsky <sky@nipapa.tw>

ENV TZ=Asia/Taipei
WORKDIR /usr/local/apache2/htdocs/
ADD ./daradish/ /usr/local/apache2/htdocs/
RUN ["make", "pull"]

CMD ["make", "run"]
