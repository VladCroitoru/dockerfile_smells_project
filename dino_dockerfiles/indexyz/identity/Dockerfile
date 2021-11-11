FROM mhart/alpine-node
MAINTAINER Indexyz <r18@indexes.nu>

ARG VCS_REF

LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="e.g. https://github.com/Indexyz/Identity"
      
RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app
RUN cd /usr/src/app && npm install

EXPOSE 8080:80

ENTRYPOINT ["node"]
CMD ["Bin/run"]
