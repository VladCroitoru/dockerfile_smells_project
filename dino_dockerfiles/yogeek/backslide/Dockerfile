FROM yogeek/nodegosu

RUN apt-get update && \
    apt-get install -y libx11-xcb-dev

# install backslide globally
RUN gosu node npm install -g backslide
