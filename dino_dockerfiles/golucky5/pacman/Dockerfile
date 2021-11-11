FROM alpine:latest
#start with a small image
MAINTAINER david <golucky@gmail.com>
#add Nginx
#add Git so that we can get code straght from the git hub
RUN apk --update add git \
        nginx
#Remove everything from the html directoy
RUN rm -rf /usr/share/nginx/html/*.*
#git clone whatever you want
RUN git clone https://github.com/golucky5/pacman.git /usr/share/nginx/html/
# it's a webserver so port 80 time
EXPOSE 80
#start command
CMD ["nginx", "-g", "daemon off;"]
