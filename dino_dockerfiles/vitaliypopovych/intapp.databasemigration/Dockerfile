FROM maven:3.3.9-jdk-8-onbuild
COPY . /usr/src/datamigrationapp
WORKDIR /usr/src/datamigrationapp
RUN mvn package
CMD ["java", "-jar", "target/Intapp.DatabaseMigration-1.0-SNAPSHOT-jar-with-dependencies.jar"]