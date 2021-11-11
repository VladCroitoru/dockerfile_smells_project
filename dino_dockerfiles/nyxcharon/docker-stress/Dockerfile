FROM alpine:3.3
RUN echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN apk add --update stress@testing python py-pip gcc python-dev  musl-dev linux-headers && rm -rf /var/cache/apk/*
RUN pip install psutil
ADD mem-fill /scripts/mem-fill
CMD stress
