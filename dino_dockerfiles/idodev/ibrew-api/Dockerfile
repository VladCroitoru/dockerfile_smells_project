FROM node


RUN apt-get update && apt-get install -y \
git \
python-setuptools \
make \
&& rm -rf /var/lib/apt/lists/* \
&& easy_install pip


RUN git clone https://github.com/Tristan79/iBrew.git ~/iBrew
RUN cd ~/iBrew/source/ && make setuplin && ln -s ~/iBrew/ibrew /usr/local/bin/ibrew


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY app /usr/src/app/
RUN ls /usr/src/app/

RUN npm install

EXPOSE 3000
CMD [ "npm", "start"]