FROM instrumentisto/glide

WORKDIR /go/src/app
COPY . .

RUN glide update --strip-vendor
RUN mkdir -p build/Linux  && GOOS=linux go build -o build/Linux/configmap-pod-restarter

ENTRYPOINT [ "/go/src/app/build/Linux/configmap-pod-restarter" ]