FROM paulflorea/python3-uwsgi:latest

# install bower & then install the components
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g bower