FROM golang:1 as terragrunt
RUN go get github.com/gruntwork-io/terragrunt
RUN CGO_ENABLED=0 GOOS=linux go build -a -ldflags '-extldflags "-static"' github.com/gruntwork-io/terragrunt

FROM hashicorp/terraform:light
RUN apk add libc6-compat
COPY --from=terragrunt /go/bin/terragrunt /bin
ENTRYPOINT ["/bin/terragrunt"]

