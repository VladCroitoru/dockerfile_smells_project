FROM countly/countly-server

# Disable mongo
RUN rm -rf /etc/service/mongodb

ADD frontend.config.js /opt/countly/frontend/express/config.js
ADD api.config.js /opt/countly/api/config.js

