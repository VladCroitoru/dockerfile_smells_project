FROM golang:1

ENV BOOKSING_BOOKDIR /books
ENV BOOKSING_DATABASEDIR /db
ENV BOOKSING_FAILDIR /failed
ENV BOOKSING_IMPORTDIR /import

WORKDIR /app

COPY . .

RUN export GOOS=linux && export GOARCH=amd64 && go mod tidy && go build -tags 'fts5' -o booksing ./cmd/ui

CMD ./booksing
