FROM maven:3-jdk-8-alpine

WORKDIR /argos-backend

COPY . .

RUN mv src/main/resources/argos-backend_template.properties src/main/resources/argos-backend.properties && \
    chmod +x scripts/docker-start.sh

EXPOSE 8989

CMD scripts/docker-start.sh