FROM golang:1.7

RUN go get "github.com/jessevdk/go-flags" "github.com/groundnuty/hipchat-api-go" "github.com/groundnuty/hipchat-docker-webhook"

ENV HIPCHAT_TOKEN="wrong_token" 	\
 HIPCHAT_ROOM="not_that_room" 		\
 WEBHOOK_AUTH_PASS="wrong_password" \
 LISTENING_ADDRESS="0.0.0.0:9443" 	\
 HIPCHAT_NOTIFY="false"

EXPOSE 9443

CMD hipchat-docker-webhook -k "$HIPCHAT_TOKEN" -r "$HIPCHAT_ROOM" -a "$WEBHOOK_AUTH_PASS" -b "$LISTENING_ADDRESS"