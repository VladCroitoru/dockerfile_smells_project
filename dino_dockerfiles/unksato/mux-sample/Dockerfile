
# golang:onbuild automatically copies the package source, 
# fetches the application dependencies, builds the program, 
# and configures it to run on startup 
FROM golang:onbuild
LABEL Name=mux-sample Version=0.0.1 
RUN mkdir /app 
ADD . /app/ 
WORKDIR /app 
RUN go build -o mux-sample .
EXPOSE 8080 
CMD ["/app/mux-sample"]
