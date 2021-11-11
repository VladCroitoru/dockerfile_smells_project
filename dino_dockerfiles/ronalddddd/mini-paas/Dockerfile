FROM hashicorp/terraform:full

RUN go get -u github.com/squat/terraform-provider-vultr
ADD .terraformrc /root/.

RUN mkdir /deployment
ADD tf_modules /tf_modules

WORKDIR /deployment
ENTRYPOINT /bin/sh
