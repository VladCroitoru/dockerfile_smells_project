FROM nginx:latest
EXPOSE 80
ENV HTML=/mnt
#RUN echo "non cosi' bellaaaaa 4" > /usr/share/nginx/html/index.html
CMD echo ${HTML} && cp -arf ${HTML}/* /usr/share/nginx/html/ && chown -R nginx: /usr/share/nginx/html && ls -la /usr/share/nginx/html && nginx -g 'daemon off;'
