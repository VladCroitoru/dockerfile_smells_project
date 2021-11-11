FROM busybox
EXPOSE 10100
EXPOSE 10101
VOLUME /etc/redirect
ADD redirect /bin/

CMD ["/bin/redirect", "-config", "/etc/redirect/config.json", "-ui-addr", "0.0.0.0:10101", "-bind", "0.0.0.0:10100"]
