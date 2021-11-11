FROM alpine:latest
LABEL maintainer="gwaewion@gmail.com"
EXPOSE 27017
COPY run.sh /root
VOLUME /data

ENV ADMINUSER admin
ENV ADMINPASS admin_password
ENV REGULARUSER vl
ENV REGULARPASS vl_password

RUN apk update
RUN apk add mongodb sudo
RUN chown -R mongodb:mongodb /data

CMD ["sh", "/root/run.sh"]
