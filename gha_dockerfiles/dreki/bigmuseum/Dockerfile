FROM python:3.9-alpine3.14

# FROM node:14-alpine
# ENV NODE_ENV=production
# WORKDIR /usr/src/app
# COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]
# RUN npm install --production --silent && mv node_modules ../
# COPY . .
# EXPOSE 8888
# RUN chown -R node /usr/src/app
# USER node
# CMD ["npm", "start"]

ENV VIRTUAL_ENV="/opt/venv"
RUN /usr/local/bin/python3 -m venv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

RUN set -x \
  && apk add --no-cache bash nodejs \
  && apk add --no-cache npm \
  && apk add --no-cache util-linux \
  && apk add --no-cache build-base \
  && npm install --global yarn

# WORKDIR here is important for installing node packages
WORKDIR /
COPY package.json package.json
# Install Node dependencies at `/node_modules` in the container.
RUN set -x \
  && yarn install --modules-folder=/node_modules
ENV PATH="/node_modules/.bin:${PATH}"

# Use Python venv when connecting to this container via shell.
RUN set -x \
  && echo "#!/usr/bin/which bash" > /root/.bashrc \
  && echo "PS1=\"\w # \"" > /root/.bashrc \
  && echo ". ${VIRTUAL_ENV}/bin/activate" >> /root/.bashrc \
  && chmod u+rx /root/.bashrc


WORKDIR /app

# Install Python requirements.
COPY requirements.txt requirements.txt
RUN set -x \
  && pip3 install --upgrade pip \
  && pip3 install ipython \
  && pip3 install -r requirements.txt

# Install Node requirements.
# COPY package.json package.json
# RUN set -x \
#   && npm install --global yarn
# && npm install

COPY . /app

# CMD ["python3", "/app/main.py"]
CMD ["/app/main.sh"]
