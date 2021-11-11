FROM base/archlinux

RUN pacman -Syu --noconfirm && pacman -S bash tor vim python2-gevent python2-msgpack python2-pyopenssl --noconfirm && paccache -r -k 0
COPY inits /sbin/inits 
RUN chmod +x /sbin/inits
RUN mkdir -p /tapone && chmod g+ws /tapone

 WORKDIR /tapone

 ENTRYPOINT ["/sbin/inits"]

#Expose ports
EXPOSE 43110  16943
