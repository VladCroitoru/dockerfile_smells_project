FROM public.ecr.aws/lambda/go:1 as build
# install compiler
RUN yum install -y golang
RUN go env -w GOPROXY=direct
# cache dependencies
ADD src/go.mod src/go.sum ./
RUN go mod download
# build
ADD src/. .
RUN go build -o /main

FROM public.ecr.aws/lambda/go:1
COPY --from=build /main /main
ARG COMMIT_HASH
ENV COMMIT_HASH=$COMMIT_HASH