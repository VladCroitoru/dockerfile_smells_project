FROM node:4

MAINTAINER Nils Haukaas <mail@nilsnh.no>

RUN npm install bower -g 

# Silence the bower used as root warning
RUN echo '{ "allow_root": true }' > /root/.bowerrc

# Bower will try to create this folder and fail if it's
# not there and editable. 
RUN mkdir .config .cache .local \
	&& chown 1000 -R /.config \
	&& chown 1000 -R /.cache \
	&& chown 1000 -R /.local

