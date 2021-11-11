FROM mjrodgers1/nodejs:v1036
MAINTAINER Mark Rodgers <mark.rodgers@irishlife.ie>

# pull down the code from github; specifically the webservice 
RUN wget https://raw.githubusercontent.com/mjrodgers1/docker-demo/master/service.js \
    --no-check-certificate

# something should be able to attach to this port
EXPOSE 8888

CMD ["node/bin/node", "service.js"]