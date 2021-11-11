FROM almalinux:8

RUN curl https://nodejs.org/dist/v12.22.1/node-v12.22.1-linux-x64.tar.gz -o /root/node.tar.gz && \
    cd /usr/local && tar --strip-components 1 -xzf /root/node.tar.gz
RUN npm install -g -y @quasar/cli
WORKDIR /code

# CMD ["/bin/bash"]
CMD ["npm", "run", "build"]
# docker run --rm -it -v $(pwd):/code -p 8080:8080 7ce58f1d59e9
