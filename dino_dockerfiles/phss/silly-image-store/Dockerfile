FROM dockerfile/java:oracle-java8

# Build standalone server jar
ADD . /opt/app
WORKDIR /opt/app
RUN ./lein.sh ring uberjar

# Start app
EXPOSE 3000
CMD java -Dbase.store.dir=/opt/images/ -jar /opt/app/target/silly-image-store-*-SNAPSHOT-standalone.jar

