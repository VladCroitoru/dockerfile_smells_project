FROM toksaitov/auca-judge-back

WORKDIR /auca-judge-queue

COPY package.json /auca-judge-queue
RUN npm install

COPY . /auca-judge-queue
ENV AUCA_JUDGE_QUEUE_BACK_SERVER http://localhost:7070

CMD ["npm", "start"]
