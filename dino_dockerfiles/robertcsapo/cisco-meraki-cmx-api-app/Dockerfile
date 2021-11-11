FROM ruby:2.3
MAINTAINER Robert (robert@nigma.org)

EXPOSE 4567

# Installing ruby gems
RUN DEBIAN_FRONTEND=noninteractive gem install sinatra --version 1.4.8
RUN DEBIAN_FRONTEND=noninteractive gem install data_mapper
RUN DEBIAN_FRONTEND=noninteractive gem install dm-sqlite-adapter
RUN DEBIAN_FRONTEND=noninteractive gem install thin
RUN DEBIAN_FRONTEND=noninteractive git clone https://github.com/meraki/cmx-api-app.git

# Google Maps API added
COPY public/index.html /cmx-api-app/public/index.html

# Zoom out and have the world as default center (not Meraki HQ)
COPY public/sample.js /cmx-api-app/public/sample.js

COPY cmx_app_start.sh /cmx-api-app/
CMD bash /cmx-api-app/cmx_app_start.sh
