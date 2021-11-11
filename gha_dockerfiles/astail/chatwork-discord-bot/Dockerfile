FROM java:8-jre
COPY ./target/universal/chatwork-discord-bot-0.1.0-SNAPSHOT.zip /usr/src/myapp/chatwork-discord-bot-0.1.0-SNAPSHOT.zip
WORKDIR /usr/src/myapp
RUN unzip /usr/src/myapp/chatwork-discord-bot-0.1.0-SNAPSHOT.zip
RUN rm /usr/src/myapp/chatwork-discord-bot-0.1.0-SNAPSHOT.zip

CMD ["/usr/src/myapp/chatwork-discord-bot-0.1.0-SNAPSHOT/bin/chatwork-discord-bot"]
