FROM php:7.0.22-alpine

#Update apk
RUN apk update

#PIP 
RUN apk add --update \
    python \    
    py-pip

#AWS and ESC CLI's
RUN pip install awscli --upgrade --user
RUN curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-cli/ecs-cli-linux-amd64-latest
RUN chmod +x /usr/local/bin/ecs-cli
ENV PATH ~/.local/bin:$PATH
ENV PATH /root/.local/bin:$PATH

#GIT
RUN apk add git

#Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

#Zip (used as fallback by composer)
RUN apk add zip

#Node
RUN apk add nodejs
