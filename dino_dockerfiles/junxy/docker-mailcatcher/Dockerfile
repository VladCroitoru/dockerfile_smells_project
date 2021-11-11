FROM quay.io/sameersbn/ubuntu:14.04.20151023
MAINTAINER Junior Xu "ayijun@gmail.com"

ADD install.sh install.sh
RUN chmod +x install.sh && ./install.sh && rm install.sh

# smtp port
EXPOSE 1025

# webserver port
EXPOSE 1080

CMD ["mailcatcher", "-f", "--ip=0.0.0.0"]
