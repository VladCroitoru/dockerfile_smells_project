FROM justbuchanan/docker-archlinux

# install system deps and clear cache
RUN pacman -Syu --noconfirm nodejs yarn gcc go git
RUN pacman -Scc --noconfirm

# angular-cli
RUN yarn global add @angular/cli && ng version

ENV GOPATH=/go

# relocate into correct dir in go path
ENV DIR=$GOPATH/src/github.com/justbuchanan/winesnob
RUN mkdir -p $DIR
WORKDIR $DIR

# node deps
COPY package.json yarn.lock ./
RUN yarn install

COPY wine-list.json ./

COPY backend ./backend
RUN go get -v ./backend/...
RUN go build -o winesnob-backend ./backend

# copy frontend files and compile, resulting in a statically-servable "dist" directory
COPY protractor.conf.js tslint.json karma.conf.js angular-cli.json ./
COPY src ./src
RUN ng build --env=prod

VOLUME "/data"
VOLUME "/etc/cellar-config.json"
EXPOSE 80
CMD ["./winesnob-backend", "--dbpath", "/data/cellar.sqlite3db", "--config", "/etc/cellar-config.json", "--port=80"]
