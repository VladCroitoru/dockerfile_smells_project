FROM alpine:3.4

RUN apk add --no-cache python py-pip grep gawk

RUN mkdir /tailon 
COPY run.sh /tailon/run.sh
RUN chmod +x /tailon/run.sh
COPY tailon-1.1.1 /tailon/tailon-1.1.1
RUN pip install /tailon/tailon-1.1.1

VOLUME ["/data"]

EXPOSE 8080

WORKDIR "/tailon"

CMD ["/tailon/run.sh"]

USER nobody

# docker run -it -v /var/log:/data --user=1000 -p 8084:8080 sago007/docker_tailon
