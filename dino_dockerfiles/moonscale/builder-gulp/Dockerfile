FROM node:0.10

RUN apt-get update && \
    DEBIAN_FRONTEND=non-interactive apt-get install ruby-full -y && \
    apt-get clean

RUN gem install sass

RUN npm install -g npm@next && npm install -g bower && npm install -g gulp-cli

RUN echo "user0:x:1000:1000:User 0:/tmp:/bin/false" >> /etc/passwd && \
    echo "user1:x:1001:1001:User 1:/tmp:/bin/false" >> /etc/passwd && \
    echo "user2:x:1002:1002:User 2:/tmp:/bin/false" >> /etc/passwd && \
    echo "user3:x:1003:1003:User 3:/tmp:/bin/false" >> /etc/passwd && \
    echo "user4:x:1004:1004:User 4:/tmp:/bin/false" >> /etc/passwd
