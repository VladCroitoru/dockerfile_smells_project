FROM alpine:3.4

RUN apk add --no-cache python3 &&\
    pip3 install apscheduler &&\
    pip3 install requests

COPY pagespeed.py pagespeed.conf /

EXPOSE 9113

CMD python3 /pagespeed.py
