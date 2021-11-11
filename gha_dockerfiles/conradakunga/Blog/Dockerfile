FROM jekyll/jekyll
COPY Gemfile Gemfile.lock /srv/jekyll/
#RUN apk -U upgrade
RUN apk add rsync
RUN apk add sshpass
RUN apk add openssh 

ARG SSH_PRIVATE_KEY
RUN mkdir ~/.ssh/
RUN echo "${SSH_PRIVATE_KEY}" > ~/.ssh/id_rsa
RUN touch ~/.ssh/known_hosts
RUN ssh-keyscan hairofthedog.dreamhost.com >> /root/.ssh/known_hosts
RUN chmod 700 /root/.ssh
#chmod 644 ~/.ssh/id_rsa.pub
RUN chmod 600 ~/.ssh/id_rsa

RUN bundle config set path vendor/bundle && bundle install