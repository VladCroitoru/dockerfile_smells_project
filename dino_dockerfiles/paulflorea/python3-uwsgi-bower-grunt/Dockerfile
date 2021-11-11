FROM paulflorea/python3-uwsgi-bower:latest

# install ruby, sass, compass
RUN apt-get install -y ruby-full; gem update --system; gem install compass

RUN npm install -g grunt-cli
