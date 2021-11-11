FROM node

WORKDIR /srv/banditio.web/devtools
ADD https://chromium.googlesource.com/chromium/blink/+archive/9c1f3db8fdeaaf3e74f5dc0f6e71cba556569ad2/Source/devtools/front_end.tar.gz /srv/banditio.web/devtools/front_end.tar.gz
RUN cd /srv/banditio.web/devtools && tar xvfz front_end.tar.gz
ADD . /srv/banditio.web
RUN npm install

EXPOSE 4000
WORKDIR /srv/banditio.web/

# Default command
CMD ["node", "/srv/banditio.web/app.js"]
#CMD ["/usr/bin/supervisord"]
#CMD ["bash"]