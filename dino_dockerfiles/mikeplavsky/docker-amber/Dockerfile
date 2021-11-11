FROM mikeplavsky/nodejs

RUN npm install -g amber-cli

ADD bowerrc /root/.bowerrc
ADD app /

WORKDIR  /app
CMD amber serve

