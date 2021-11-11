FROM ubuntu:16.04
# nooo, ubuntu is not overkill at all

RUN apt-get update && apt-get install -y socat redis-tools

COPY lol.sh /
RUN chmod +x /lol.sh

EXPOSE 5000

CMD ["socat", "TCP-LISTEN:5000,fork,reuseaddr", "EXEC:/lol.sh"]
