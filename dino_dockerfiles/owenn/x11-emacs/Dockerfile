FROM alpine:3.7

MAINTAINER Nigel Owen nigelowen2@gmail.com

RUN apk update # may as well split the lines up, the update is pretty small
RUN apk add ca-certificates emacs-gtk2 curl bash xclock git aspell aspell-en libc-dev go openssh 

WORKDIR /home/developer

COPY init.el /root/.emacs.d/
COPY entrypoint.sh /

ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "emacs" ]
