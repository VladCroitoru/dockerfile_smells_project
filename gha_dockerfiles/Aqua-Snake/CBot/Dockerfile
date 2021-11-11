FROM fusuf/whatsasena:latest

RUN git clone https://github.com/Aqua-Snake/CBot /root/CBot
WORKDIR /root/CBot/
ENV TZ=Asia/Kolkata
RUN npm install supervisor -g
RUN yarn install --no-audit

CMD ["node", "bot.js"]
