FROM alpine:3.6

#Install ZeroNet
RUN apk --update upgrade \
  && apk --no-cache --no-progress add musl-dev gcc python python-dev py2-pip tor git openssl curl dumb-init \
  && git clone https://github.com/HelloZeroNet/ZeroNet /zn && cd /zn \
  && pip install -r requirements.txt \
  && apk del musl-dev gcc python-dev py2-pip git \
  && rm -rf /var/cache/apk/* /tmp/* /var/tmp/* /root/* \
  && echo "ControlPort 9051" >> /etc/tor/torrc \
  && echo "CookieAuthentication 1" >> /etc/tor/torrc

#Control if Tor proxy is started
ENV ENABLE_TOR false
ENV HOME /zn

WORKDIR /zn

#Set upstart command
ENTRYPOINT ["/usr/bin/dumb-init","/usr/bin/python","zeronet.py"]
CMD ["--ui_ip","0.0.0.0"]

#Expose ports
EXPOSE 43110 15441
