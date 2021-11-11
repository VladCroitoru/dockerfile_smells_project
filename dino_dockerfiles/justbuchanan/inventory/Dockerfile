FROM justbuchanan/docker-archlinux

RUN pacman -Syu --noconfirm
RUN pacman -S --noconfirm nodejs gcc python python-pip go git python2 yarn

ENV GOPATH $HOME/go
RUN go get github.com/gorilla/mux \
    github.com/gorilla/handlers \
    github.com/jinzhu/gorm \
    github.com/jinzhu/gorm/dialects/sqlite

RUN yarn global add @angular/cli
RUN ng version

RUN mkdir inventory
WORKDIR inventory

COPY dymo-labelgen ./dymo-labelgen
RUN pip install -r dymo-labelgen/requirements.txt

COPY package.json yarn.lock ./
RUN yarn install

COPY backend ./backend

# copy frontend files and compile, resulting in a statically-servable "dist" directory
COPY protractor.conf.js tslint.json karma.conf.js angular-cli.json ./
COPY src ./src
# TODO: fix ng build
RUN ng build --env=prod

VOLUME "/data"
EXPOSE 8080
CMD ["go", "run", "backend/main.go", "--dbpath", "/data/parts.sqlite3db"]
