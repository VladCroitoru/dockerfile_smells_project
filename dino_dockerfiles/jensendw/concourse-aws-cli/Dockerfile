FROM alpine:3.6
LABEL Name="concourse-aws-cli"
LABEL Version="0.2"
RUN apk update && apk add python py-pip
RUN pip install awscli==1.11.168 --upgrade 
EXPOSE 0
CMD ["/bin/sh"]

