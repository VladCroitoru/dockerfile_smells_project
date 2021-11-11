FROM node:6.11
RUN git clone https://github.com/n1k0/readable-proxy ; cd readable-proxy ; npm install
RUN git clone https://github.com/mozilla/readability.git
# ADD timeout.patch /timeout.patch
# ADD maxbuffer.patch /maxbuffer.patch
# RUN cd readable-proxy ; patch -p0 < /timeout.patch
# RUN cd readable-proxy ; patch -p1 < /maxbuffer.patch
WORKDIR /readable-proxy
ENV READABILITY_LIB_PATH /readability/Readability.js
CMD ["npm", "start"]
