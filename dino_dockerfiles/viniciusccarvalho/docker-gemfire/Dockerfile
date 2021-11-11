FROM java:8
VOLUME /tmp
EXPOSE 8080 1099 10334 40404
ADD config/cache.properties config/cache.properties
ADD config/cache-context.xml config/cache-context.xml
ADD scripts/run.sh run.sh
ADD build/libs/gemfire-boot-server-8.1.0.jar gemfire-server.jar
CMD ["/run.sh"]