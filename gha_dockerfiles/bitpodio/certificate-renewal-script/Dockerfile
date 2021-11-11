# FROM bitpod/nginx-nodejs:latest
FROM certbot/dns-google:v1.18.0

ENV app="/opt/certbot"

RUN apk add --update \
 curl \
 which \
 bash
 
RUN curl -sSL https://sdk.cloud.google.com | bash

ENV PATH $PATH:/root/google-cloud-sdk/bin

COPY ["./main.sh", "$app/"]

RUN sed -i 's/\r$//' $app/main.sh  && \  
    chmod +x $app/main.sh

#CMD ["sh" , "main.sh"]
