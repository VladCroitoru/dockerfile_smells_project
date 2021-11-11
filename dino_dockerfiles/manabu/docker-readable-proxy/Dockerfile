FROM node:6.9.5
RUN git clone https://github.com/n1k0/readable-proxy ; cd readable-proxy ; npm install
ADD timeout.patch /timeout.patch
ADD maxbuffer.patch /maxbuffer.patch
RUN cd readable-proxy ; patch -p0 < /timeout.patch
RUN cd readable-proxy ; patch -p1 < /maxbuffer.patch
WORKDIR /readable-proxy
CMD ["npm", "start"]
