FROM node:latest

RUN git clone --depth=1 https://github.com/UniversityRadioYork/ury-hubot.git
WORKDIR ury-hubot
ENTRYPOINT ["bin/hubot", "-a", "slack"]
