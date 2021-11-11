FROM hasholding/alpine-base

LABEL maintainer "Levent SAGIROGLU <LSagiroglu@gmail.com>"

ARG VERSION=1.4.0
ENV KAPACITOR_CONFIG_PATH /etc/kapacitor.conf
VOLUME ["/shared","/shared/replay"]
WORKDIR /tmp
RUN apk add --no-cache wget 
RUN wget https://dl.influxdata.com/kapacitor/releases/kapacitor-${VERSION}-static_linux_amd64.tar.gz -O kapacitor.tar.gz
RUN tar xvfz kapacitor.tar.gz -C /bin --strip 2
RUN rm -r *
COPY kapacitor.conf /etc/kapacitor.conf
EXPOSE 9092
ENTRYPOINT ["/bin/kapacitord"]