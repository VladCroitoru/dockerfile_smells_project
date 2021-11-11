FROM alpine:latest
MAINTAINER Ryan Meharg <ryan.meharg@altoros.com>

# Update and install base packages
RUN apk update && apk upgrade && apk add --no-cache curl bash make gnupg git g++ make openssh openssl openssl-dev

# Add yaml-patch
ADD https://github.com/krishicks/yaml-patch/releases/download/v0.0.10/yaml_patch_linux /usr/local/bin/yaml-patch
RUN chmod u+x /usr/local/bin/yaml-patch

# Add fly cli
ADD https://github.com/concourse/concourse/releases/download/v3.9.1/fly_linux_amd64 /usr/local/bin/fly
RUN chmod u+x /usr/local/bin/fly
