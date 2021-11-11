FROM ubuntu:16.04
MAINTAINER yivanus yivanus@gmail.com 
RUN mkdir -p /var/mindx/meteor && chmod 777 /var/mindx/meteor 
RUN apt-get update && apt-get install -y git 
ENV HOME /var/mindx/meteor
ENV LC_ALL "C"
RUN useradd mindx
USER mindx
RUN curl https://install.meteor.com | sh
WORKDIR /var/mindx/meteor
RUN git clone https://github.com/yivanus/kityminder-meteor.git
ENV PATH $PATH:$HOME/.meteor
RUN meteor create --bare /var/mindx/meteor/kityminder-meteor-demo
WORKDIR /var/mindx/meteor/kityminder-meteor-demo/
RUN meteor remove blaze-html-templates && meteor add angular-templates && meteor npm install --save angular angular-meteor && meteor add iron:router && meteor add meteorhacks:picker && meteor add session && meteor add autopublish 
WORKDIR /var/mindx/meteor/kityminder-meteor 
RUN cp -r -f README.md client collection packages.json server public /var/mindx/meteor/kityminder-meteor-demo/ 
WORKDIR /var/mindx/meteor/kityminder-meteor-demo/ 

RUN meteor add meteorhacks:npm && meteor update meteorhacks:npm && meteor 

RUN echo "#! /bin/bash" > /var/mindx/meteor/meteor.sh && echo "cd /var/mindx/meteor/kityminder-meteor-demo" >> /var/mindx/meteor/meteor.sh  && echo "meteor run -p 8899" >> /var/mindx/meteor/meteor.sh 
RUN chmod +x /var/mindx/meteor/meteor.sh
RUN echo `cat /var/mindx/meteor/meteor.sh`
EXPOSE 8899 
CMD "/var/mindx/meteor/meteor.sh"
