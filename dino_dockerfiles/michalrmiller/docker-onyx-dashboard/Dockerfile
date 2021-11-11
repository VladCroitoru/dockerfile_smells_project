FROM java:8

ENV VERSION=0.9.9.0

RUN wget -O /onyx-dashboard.jar https://s3-us-west-1.amazonaws.com/onyx-releases/onyx-dashboard/onyx-dashboard-$VERSION.jar

EXPOSE 3000

ENTRYPOINT ["java", "-server", "-jar", "/onyx-dashboard.jar"]

CMD ["$ZOOKEEPER_ADDR"]