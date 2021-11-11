FROM node:carbon

# Install app dependencies
RUN  git clone https://github.com/TampereTC/tre-smartcity-backEnd && \
	 cd tre-smartcity-backEnd

WORKDIR tre-smartcity-backEnd
RUN	 npm install

# If you are building your code for production
#RUN npm install --only=production

VOLUME ["tre-smartcity-backEnd"]
EXPOSE 3001
CMD [ "npm", "start" ]

