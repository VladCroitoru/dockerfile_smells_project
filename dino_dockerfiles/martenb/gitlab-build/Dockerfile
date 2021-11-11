FROM alpine:latest

RUN apk --no-cache add lftp ca-certificates openssh wget

#RUN mkdir ~/.lftp && (echo "set ftp:ssl-allow true") >> ~/.lftp/rc && (echo "set ssl:verify-certificate false") >> ~/.lftp/rc

RUN mkdir ~/.lftp && (echo "set ftp:ssl-allow false") >> ~/.lftp/rc
