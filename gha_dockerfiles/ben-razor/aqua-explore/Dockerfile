FROM python:3 

RUN apt-get update && apt-get install -y \
    software-properties-common \
    npm

RUN npm install npm@latest -g && \
    npm install n -g && \
    n latest

RUN npm -g install @fluencelabs/aqua

RUN npm -g install @fluencelabs/aqua-lib

COPY ./scripts/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /opt/aqua-compile

EXPOSE 8866
EXPOSE 8868

ENTRYPOINT /opt/aqua-compile/scripts/start_frontend_server