FROM imsky/haxe
MAINTAINER emmanuel.botros@gmail.com
WORKDIR /application

# prerequistes
RUN apt-get update && apt-get install -y git python-pip gyp npm nodejs

# nvm env
ENV NODE_VER v4.2.3
RUN git clone https://github.com/creationix/nvm.git $HOME/.nvm
RUN echo '. ~/.nvm/nvm.sh' >> $HOME/.profile
RUN echo 'nvm install ${NODE_VER}' >> $HOME/.profile
RUN echo 'nvm alias default ${NODE_VER}' >> $HOME/.profile

# python
RUN PYTHON=$PYTHON:/usr/bin/python
RUN export PYTHON

# npm libs
RUN npm install --unsafe-perm -g gulp  
RUN npm install --unsafe-perm node-gyp 
RUN npm install --unsafe-perm microtime  
RUN npm install --unsafe-perm -g sqlite3
RUN npm install --unsafe-perm -g mssql
#RUN npm install --unsafe-perm -g https://github.com/RuntimeTools/appmetrics
#RUN npm install --unsafe-perm -g appmetrics-elk

RUN rm -rf *
RUN git clone https://github.com/mebyz/pistahx-app . && git fetch && git checkout 9e05f94

# app dependencies
RUN npm install --unsafe-perm --only=dev

# haxe libs
RUN echo "y" | haxelib install ./node_modules/pistahx/gen/libs.hxml

RUN npm install sqlite3 tedious

RUN gulp build

RUN gulp pack

RUN cp -rf node_modules/* distrib/out/node_modules/

RUN cp -rf distrib/out/* /application/

ENV ENV localdocker

EXPOSE  3000

CMD ["node", "/application/app.js"]
