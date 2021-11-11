FROM tquinlan1992/debian-nvm

COPY . /server-app/

RUN . /etc/profile && \
	cd /server-app && \
	nvm install && \
	npm install && \
	npm test && \
    npm run build

EXPOSE 8000

CMD . /etc/profile \
    && cd /server-app \
    && nvm use \
    && npm start
