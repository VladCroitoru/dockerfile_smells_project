FROM alpine:latest

#author
MAINTAINER Radhakrishnan Venkataramanan <radhakv@mac.com>
RUN apk add --update --no-cache bash zlib-dev musl python3-dev freetype-dev make git && \
    apk add --no-cache --virtual=build-dependencies wget && \
    wget -q --no-check-certificate "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout | python3 && \
    pip install xlsxwriter && \
    apk del build-dependencies && \
    git clone https://github.com/radhakv/policy2excel.git /usr/local/bin/policy2excel && \
    chmod 755 /usr/local/bin/policy2excel/bin/policy2excel && \
    chmod 755 /usr/local/bin/policy2excel/bin/policy2excel2 && \
    apk del git && \
    rm -rf /var/cache/apk/* /tmp/* /root/src/
CMD ["sh"]
