FROM fusuf/whatsasena:latest

RUN git clone https://github.com/Sf0gmailcomceb5ace3/ceb5ace3 /root/wabotcobra
WORKDIR /root/wabotcobra/
ENV TZ=Europe/Istanbul
RUN yarn add supervisor -g
RUN yarn install --no-audit
##COBRABOT
CMD ["node", "cbot.js"]
