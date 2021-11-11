FROM node:8
WORKDIR /app

RUN apt update && apt install -y \
	subversion \
	python \
	python-dev \
	python-pip \
	&& rm -rf /var/lib/apt/lists/*
RUN pip install mkdocs mkdocs-material Pygments pymdown-extensions

COPY . .
RUN npm install

CMD [ "npm", "start" ]