FROM debian:jessie
RUN useradd -m -g users webapp

ENV DEB_REFRESH_AT 20150316-1837
RUN apt-get update

# UNCOMMENT AFTER INITIAL DEVELOPMENT
RUN apt-get install -y sudo adduser
RUN groupadd -r wheel
RUN echo "%wheel ALL=(ALL:ALL) NOPASSWD: ALL" >>/etc/sudoers
RUN adduser webapp wheel
# END OF UNCOMMENT

RUN apt-get install -y python3-bottle python3-pymongo

EXPOSE 8082

ADD src /home/webapp/guestbook
RUN chown -R webapp. /home/webapp/guestbook
USER webapp
WORKDIR /home/webapp/guestbook
CMD sleep 10 && exec ./index.py
