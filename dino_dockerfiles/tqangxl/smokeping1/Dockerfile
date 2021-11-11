#Description

#Smokeping is a tool to graph network latency over time.
#This image contains the smokeping tool and a lighttpd webserver to display the graphs.
#It was built on a alpine linux image in order to keep the image size as small as possible.
#Changed from https://github.com/tomwillfixit/smokeping

#Build : docker build -t smokeping:1.0 .

#Run : docker run -d -p 8001:80 smokeping:1.0

#Available at http://<server ip>:8000

FROM alpine:3.4

# && echo "@main1 http://dl-1.alpinelinux.org/alpine/v3.4/main/" >> /etc/apk/repositories \
# && echo "@main2 http://dl-2.alpinelinux.org/alpine/v3.4/main/" >> /etc/apk/repositories \
# && echo "@main3 http://dl-3.alpinelinux.org/alpine/v3.4/main/" >> /etc/apk/repositories \
# && echo "@main http://dl-4.alpinelinux.org/alpine/v3.4/main/" > /etc/apk/repositories \
# && echo "@main5 http://dl-5.alpinelinux.org/alpine/v3.4/main/" >> /etc/apk/repositories \

MAINTAINER tangxl99
RUN  apk add --update smokeping lighttpd perl-cgi tzdata && rm -rf /var/cache/apk/*

#Creating Directory Structure

RUN [ -d /usr/data ] || mkdir -p /usr/data && \
    [ -d /usr/cache/smokeping ] || mkdir -p /usr/cache/smokeping

#Setup smokeping directories

RUN mkdir -p /var/www/smokeping/cgi-bin && \
    cp -r /usr/share/webapps/smokeping/* /var/www/smokeping/cgi-bin/ && \
	cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime &&\
	echo "Asia/Shanghai" >  /etc/timezone &&\
    ln -s /usr/cache/smokeping /var/www/smokeping/cgi-bin/cache

#Change permissions and ownership

RUN chown -R lighttpd:lighttpd /usr/data /usr/cache /var/www/smokeping
RUN chmod -R g+ws /usr/data /usr/cache /var/www/smokeping

# Using prebaked config files since there is alot of variables to be changed.

ADD config/lighttpd.conf /etc/lighttpd/lighttpd.conf
ADD config/mod_cgi.conf /etc/lighttpd/mod_cgi.conf
ADD config/smokeping.conf /etc/smokeping/config
ADD config/services.conf /etc/smokeping/services.conf
ADD config/Targets /etc/smokeping/Targets

ADD entry.sh /tmp/entry.sh
RUN chmod 777 /tmp/entry.sh

EXPOSE 80

ENTRYPOINT /tmp/entry.sh

