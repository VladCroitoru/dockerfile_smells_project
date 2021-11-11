FROM nginx:latest
ENV TARGET_HTTP http
ENV TARGET_PORT 80
COPY nginx.conf /etc/nginx/nginx.conf
ADD run.sh /run.sh
RUN chmod 700 /run.sh

CMD ["./run.sh"]



