FROM alpine:3.3
RUN apk add --no-cache less groff py-pip bash
RUN pip install awscli
ADD start /bin/start
ENTRYPOINT [ "/bin/start" ]
