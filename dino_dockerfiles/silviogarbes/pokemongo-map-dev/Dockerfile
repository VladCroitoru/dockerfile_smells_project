FROM python:2.7-alpine
RUN apk update
RUN apk add git py-pip gcc build-base python-dev nodejs ruby ruby-dev libffi-dev
RUN apk add --no-cache ca-certificates
RUN git clone https://github.com/mchristopher/PokemonGo-Map.git -b master
WORKDIR /PokemonGo-Map
RUN pip install -r requirements.txt
RUN npm install -g grunt-cli
RUN npm install
# RUN npm run-script build 
# RUN gem install travis
COPY ./entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
