FROM nginx:1.12-alpine
MAINTAINER Said Sef <said@saidsef.co.uk> (http://saidsef.co.uk/)

LABEL version="3.3"
LABEL description="Containerised Nginx Server"

ENV HOME /tmp

# Define working directory.
WORKDIR /data

#  create build id
ARG BUILD_ID=""
RUN echo ${BUILD_ID} > build_id.txt

# Mount Nginx config
ADD config/custom.conf /etc/nginx/conf.d/

# Expose ports
# - 80: HTTP
EXPOSE 80

# Define default command
CMD ["nginx","-g","daemon off;"]
