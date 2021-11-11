# FROM openliberty/open-liberty:full-java8-openj9-ubi
# COPY src/main/liberty/config /config/
# ADD target/testwar.war /config/dropins/
# Wildfly
FROM ghcr.io/andidroid/testhollowjar:latest
COPY target/testwar.war /deployments/ROOT.war