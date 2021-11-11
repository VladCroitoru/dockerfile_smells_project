FROM onezoomin/allsync-nodejs:latest

RUN npm up && npm i -g @babel/runtime semantic-release
RUN git clone https://github.com/mdsb100/node-gitlab.git
RUN cd node-gitlab && npm install
RUN cd node-gitlab && npm run build && npm link

CMD ["/bin/bash"]
