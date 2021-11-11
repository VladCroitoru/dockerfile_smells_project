FROM node:6.6

RUN apt-get update && apt-get install -y --no-install-recommends \
	jq vim less

WORKDIR /work/

RUN npm install -g angular-cli@1.0.0-beta.24

#RUN ng new project1; exit 0
#WORKDIR /work/project1
#RUN npm install

RUN git clone https://github.com/valor-software/ng2-charts
WORKDIR /work/ng2-charts/
RUN git checkout 492aade5620670074b9fcaf961d6a6fe66aa47c7
RUN npm install
RUN npm install ng2-charts@1.5.0 --save

EXPOSE 4200 49153

CMD ["ng", "serve", "--host", "0.0.0.0", "--port", "4200", "--live-reload-port", "49153"]
