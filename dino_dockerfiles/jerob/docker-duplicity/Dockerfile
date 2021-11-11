#
#                    ##        .            
#              ## ## ##       ==            
#           ## ## ## ##      ===            
#       /""""""""""""""""\___/ ===        
#  ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ /  ===- ~~~   
#       \______ o          __/            
#         \    \        __/             
#          \____\______/                
# 
#          |          |
#       __ |  __   __ | _  __   _
#      /  \| /  \ /   |/  / _\ | 
#      \__/| \__/ \__ |\_ \__  |
#

FROM debian:jessie

MAINTAINER Jeremie Robert appydo@gmail.com version: 0.1

# Let the conatiner know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y duplicity python-boto

ADD ./duplicity /duplicity

CMD ["/bin/bash", "/duplicity"]
