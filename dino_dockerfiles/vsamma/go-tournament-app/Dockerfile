FROM golang:latest

# Copy the local package files to the container’s workspace.
ADD . /go/src/go-tournament

# Install our dependencies
#RUN go get -u github.com/go-martini/martini  
#RUN go get -u github.com/martini-contrib/binding  
#RUN go get -u github.com/martini-contrib/render  
RUN go get -u github.com/gorilla/mux
RUN go get -u gopkg.in/mgo.v2 #labix.org/v2/mgo  
#RUN go get -u github.com/go-mgo/mgo/bson #labix.org/v2/mgo/bson
#RUN go get -u 

# Install go-tournament binary globally within container 
RUN go install go-tournament

# Set binary as entrypoint
ENTRYPOINT /go/bin/go-tournament

# Expose default port (3000)
EXPOSE 3000 