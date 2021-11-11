FROM golang
RUN mkdir /app
RUN git clone https://github.com/SuriyaKalivardhan/GroupController.git /app/GroupController
WORKDIR /app/GroupController/GroupController
RUN go build
EXPOSE 5001
ENTRYPOINT ["/app/GroupController/GroupController/GroupController"]
