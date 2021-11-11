FROM nginx

MAINTAINER Chris Grimmett "chris@grimtech.net"

ADD nginx-ipfs.conf /etc/nginx/sites-available/ipfs

# create simlink to enable our config
RUN ln -s /etc/nginx/sites-available/ipfs /etc/nginx/sites-enabled/ipfs

CMD ["nginx", "-g", "daemon off;"]