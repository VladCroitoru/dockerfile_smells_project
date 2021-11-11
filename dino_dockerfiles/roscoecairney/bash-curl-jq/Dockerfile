FROM ubuntu:latest
RUN apt-get update && \
    apt-get install -y \
    jq \
    curl && \
    apt-get install ca-certificates && \
    apt-get clean

CMD ["tail -f /var/log/messages"]
