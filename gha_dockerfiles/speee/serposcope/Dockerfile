FROM amazoncorretto:8

ENV TZ=Asia/Tokyo \
    SERPOSCOPE_DB_HOST=mysql \
    SERPOSCOPE_DB_PORT=3306 \
    SERPOSCOPE_DB_USER=root \
    SERPOSCOPE_DB_PASSWORD= \
    HEAP_SIZE=2048m

EXPOSE 7134 1099 8000

VOLUME /var/log/serposcope

COPY conf/serposcope.conf /etc/serposcope/
COPY web/target/serposcope.jar /var/lib/serposcope/
COPY conf/entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
