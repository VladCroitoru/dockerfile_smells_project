FROM alpine
ADD bkpmikrotik /bkpmikrotik
RUN find bkpmikrotik -name "*.sh" -exec chmod +x {} \; && \
    apk update && \
    apk add openssh && \
    echo "0       3      *       *       *       /bkpmikrotik/scripts/bkpmktk.sh >> /files/logs.txt 2>&1" >> /etc/crontabs/root
CMD /bkpmikrotik/start.sh
