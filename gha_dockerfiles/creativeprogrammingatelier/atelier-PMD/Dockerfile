# ----- Build -----
# Using Maven on OpenJDK 11
FROM maven:3-jdk-11 AS build

WORKDIR /atelier-pmd

# Copy pom and all source files
COPY pom.xml ./
COPY src ./src

# Build the .war package
RUN mvn package -B

# ----- Release -----
# Run Tomcat 9 on OpenJDK 11
FROM tomcat:9-jdk11 AS release

# Set default configuration location
ENV ATELIER_PMD_CONFIG=/atelier-pmd/config/production.json
# Expose volume so it can be set
VOLUME /atelier-pmd/config

# Copy .war from the build stage
COPY --from=build /atelier-pmd/target/atelier-pmd.war webapps/
