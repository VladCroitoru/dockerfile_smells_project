FROM alpine
RUN apk update && apk add rclone 
ADD rclone.config /rclone.config
RUN mkdir -p /root/.config/rclone/
ADD download.sh /download.sh 

CMD ["sh", "/download.sh"] 
