FROM node:5.0.0

### hubot setup ###
# add user
ENV HUBOT_HOME_DIR /home/hubot
RUN useradd -d $HUBOT_HOME_DIR -m hubot

# permission to /usr/local
#  -> because `npm install` puts the global modules to `/usr/local/lib`.
#  -> and, user have to access there
RUN chown -R hubot /usr/local

# su
USER hubot
WORKDIR $HUBOT_HOME_DIR

# install yeoman and generator
RUN npm config set registry http://registry.npmjs.org/
RUN npm install -g yo generator-hubot

# Setup hubot (with Jenkins integration scripts)
RUN mkdir ws && cd ws \
  && yo hubot --adapter=slack --defaults \
	&& curl -fSL "https://raw.githubusercontent.com/github/hubot-scripts/master/src/scripts/jenkins.coffee" -o scripts/jenkins.coffee

# Optional (if you don't need heroke-keepalive)
#RUN cd ws \
#  && npm uninstall hubot-heroku-keepalive --save \
#  && sed -i -e "/hubot-heroku-keepalive/d" external-scripts.json
  
WORKDIR $HUBOT_HOME_DIR/ws
ENTRYPOINT ["./bin/hubot", "-a", "slack"]

