FROM ubuntu:trusty
LABEL maintainer="Boik Su <boik@tdohacker.org>"

ENV HOME /root

ARG DOMAIN
ARG EMAIL
ARG MODE=dev
ARG TYPE=self
ARG KEY
ARG CRT

WORKDIR $HOME
COPY . $HOME
RUN chown www-data:www-data $HOME

RUN ./extra/provision.sh -m $MODE -c $TYPE -k $KEY -C $CRT -D $DOMAIN -e $EMAIL -s `pwd` --docker
CMD ["./extra/service_startup.sh"]