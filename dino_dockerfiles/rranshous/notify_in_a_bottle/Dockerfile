FROM rranshous/mosquitto

RUN apt-get update && apt-get install -y inotify-tools

COPY ./ /app
WORKDIR /app

ENV TOPIC fsnotify
ENV MOSQUITTO_URL mosquitto

ENTRYPOINT ["./to_mqtt"]
CMD ["/data"]
