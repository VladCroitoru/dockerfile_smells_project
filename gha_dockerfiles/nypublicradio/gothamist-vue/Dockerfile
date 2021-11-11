FROM node:14

RUN apt-get update \
    && apt-get install -y \
        curl \
        netcat \
        nginx-extras \
        python \
        python-pip \
        python-setuptools \
        unzip \
    && pip install supervisor \
    && mkdir -p /code

WORKDIR /code

COPY package.json ./

RUN npm install 

COPY . ./
RUN rm /etc/nginx/nginx.conf \
    && ln -sf /code/nginx/* /etc/nginx/

RUN ./scripts/devenv.sh
EXPOSE 3000
ENTRYPOINT ["./scripts/entrypoint.sh"]
