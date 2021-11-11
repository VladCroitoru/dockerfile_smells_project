FROM	    node:8.9.4-alpine
LABEL       Author="Pedro Flores <pflores@codelab.com.py>"
ADD         .   /home/node/app
WORKDIR     /home/node/app
RUN         chown -R node.node .
USER        node
RUN         npm install
CMD         [ "npm", "start" ]
