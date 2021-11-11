FROM asakaguchi/docker-nodejs-hello-world

ADD https://github.com/groovenauts/magellan-proxy/releases/download/v0.1.1/magellan-proxy-0.1.1_linux-amd64 /usr/app/magellan-proxy
RUN chmod +x /usr/app/magellan-proxy

ENTRYPOINT ["/usr/app/magellan-proxy", "--port", "3000"]
CMD ["npm", "start"]
