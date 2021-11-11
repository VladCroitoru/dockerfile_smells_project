# hub.docker.com/r/itsjustcon/node-xvfb
# =====================================
# HOW TO BUILD:
#     docker build --tag=itsjustcon/node-xvfb .
# HOW TO DEPLOY:
#     docker push itsjustcon/node-xvfb

FROM node:6

# Electron support (from: http://askubuntu.com/a/510186)
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update -y && \
    apt-get install -y google-chrome-stable xvfb
