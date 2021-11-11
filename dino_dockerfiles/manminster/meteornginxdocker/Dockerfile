############################################################
# Dockerfile to build NginX based on Ubuntu 14.04 image
############################################################

FROM ubuntu:14.04

MAINTAINER manminster

# Update
RUN apt-get update -y

# Install dpenedencies
RUN apt-get install -y vim wget dialog net-tools

# Download and install nginx
RUN apt-get install -y nginx

# Remove the default Nginx configuration file, operate verbosely
RUN rm -v /etc/nginx/nginx.conf

# Copy a configuration file from the current directory into the /etc/nginx/ directory of the container
ADD nginx.conf /etc/nginx/

# Add SSl certificate and private key into directory
# ssl_certificate =>  /etc/ssl/certs/ssl-bundle.crt;
# ssl key         =>  /etc/ssl/private/myserver.key;

Add sslcerts/ssl-bundle.crt  /etc/ssl/certs/ssl-bundle.crt
ADD sslcerts/myserver.key /etc/ssl/private/myserver.key


# Expose HTTP and SSL ports
EXPOSE 80 443

# Start the nginx server after container creation
CMD service nginx start

