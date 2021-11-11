# This is a comment
FROM ubuntu

MAINTAINER lisa080404<yansha900423@163.com>

# RUN apt-get update; \
#     apt-get -y upgrade

# RUN apt-get -y install g++ BubbleTree git subversion

RUN apt-get update && apt-get install -y git

RUN mkdir -p /Users/lyan013/site/git; \
    cd /Users/lyan013/site/git; \
    sudo git clone https://github.com/lisa080404/BubbleTree.git -b master; \
    cd BubbleTree 
    # ; \
    # composer update; \
    # foreman start web

# CMD ["/Users/lyan013/site/git/BubbleTree/module_xxx/module_xxx", "--config", "/etc/module_xxx.conf"]
