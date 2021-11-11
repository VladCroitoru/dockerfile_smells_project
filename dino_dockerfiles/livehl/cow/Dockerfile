FROM alpine
copy ["cow", "/bin/cow"]
copy ["kcp", "/bin/kcp"]
copy ["start.sh", "/root/start.sh"]
copy ["rc", "/root/.cow/rc.temp"]
run ["chmod", "+x","/bin/cow"]
run ["chmod", "+x","/bin/kcp"]
run ["chmod", "+x","/root/start.sh"]
RUN apk add --no-cache  gettext bash
EXPOSE 80
EXPOSE 90
CMD ["/bin/bash","-c", "envsubst < /root/.cow/rc.temp > /root/.cow/rc && /root/start.sh"]
