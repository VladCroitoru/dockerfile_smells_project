FROM golang:1.9

RUN go get -d -v github.com/leesper/holmes
RUN go get -d -v github.com/urfave/negroni
RUN go get -d -v gopkg.in/mgo.v2
RUN go get -d -v gopkg.in/mgo.v2/bson
RUN go get -d -v github.com/dgrijalva/jwt-go
RUN go get -d -v github.com/gorilla/mux
RUN go get -d -v github.com/leesper/baidupush-golang
RUN go get -d -v github.com/leesper/gonzh
RUN go get -d -v github.com/leesper/gopay/ali
RUN go get -d -v github.com/leesper/gopay/wx
RUN go get -d -v github.com/leesper/goyht
RUN go get -d -v github.com/ltt1987/alidayu
RUN go get -d -v github.com/sideshow/apns2
RUN go get -d -v github.com/sideshow/apns2/certificate
RUN go get -d -v github.com/sideshow/apns2/payload
RUN go get -d -v gopkg.in/validator.v2
RUN go get -d -v github.com/finalsatan/Aliyun_MNS_SMS/sms
RUN go get -d -v github.com/Shopify/sarama
RUN go get -d -v golang.org/x/crypto/bcrypt
RUN go get -d -v golang.org/x/crypto/pbkdf2
RUN go get -d -v golang.org/x/crypto/blowfish
RUN go get -d -v golang.org/x/crypto/pkcs12

CMD ["go", "list", "./..."]
