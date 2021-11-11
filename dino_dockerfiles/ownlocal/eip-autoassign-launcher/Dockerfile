FROM alpine:3.4

WORKDIR /root

RUN apk --update --no-cache add py-pip && pip install aws-ec2-assign-elastic-ip

ADD entrypoint.sh /root/

ENTRYPOINT [ "./entrypoint.sh" ] # Provide "docker run" arguments when running
