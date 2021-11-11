FROM juniper/pyez

MAINTAINER Hassan El Karhani <hkarhani@gmail.com>

RUN apk add --update alpine-sdk libevent-dev linux-headers
RUN pip install zerorpc jxmlease
RUN mkdir -p /zpyez 

ADD zpyez.py /zpyez 
RUN chmod +x /zpyez/zpyez.py

EXPOSE 8484

WORKDIR /zpyez
CMD python zpyez.py 
