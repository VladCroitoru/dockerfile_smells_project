FROM python:2
MAINTAINER John McEleney <john.mceleney@netservers.co.uk>
RUN apt-get update && apt-get install -y samba-client \
  && mkdir -p /var/lib/samba/private \
  && touch /var/lib/samba/private/secrets.tdb
RUN cd /opt && git clone https://github.com/netservers/ad-password-changer.git
RUN cd /opt/ad-password-changer \
  && mkdir env && virtualenv env \
  && ./env/bin/pip install -r requirements.txt
EXPOSE 7777
WORKDIR /opt/ad-password-changer/
ENTRYPOINT ["/opt/ad-password-changer/env/bin/uwsgi","-w", "app:app", "-H", "/opt/ad-password-changer/env"]
CMD ["--http", "0.0.0.0:7777", "--enable-threads"]
