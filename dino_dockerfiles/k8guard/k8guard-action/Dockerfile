
FROM alpine
RUN apk -U add ca-certificates
ADD k8guard-action /
EXPOSE 3000
CMD ["/k8guard-action"]


# Commmenting out the multistage build 
# Unfortunately I have to revert multistage dockerfile with a lot of saddness
# because minikube uses a very old version of docker in the virtual machine they provide
# and that breaks buidling k8guard for minikube locally,
# altenrative solution would have been providing two dockerfiles one for docker-compose one for minikube
# for the sake of unity, I compromise for not using multistage dockerfile for now.
# with a lot of saddness. :(
# https://github.com/k8guard/k8guard-start-from-here/issues/50

# FROM varikin/golang-glide-alpine AS build
# WORKDIR /go/src/github.com/k8guard/k8guard-action
# COPY ./ ./
# RUN apk -U add make
# RUN make deps build
#
# FROM alpine
# RUN apk -U add ca-certificates
# COPY --from=build /go/src/github.com/k8guard/k8guard-action/k8guard-action /
# EXPOSE 3000
# CMD ["/k8guard-action"]
