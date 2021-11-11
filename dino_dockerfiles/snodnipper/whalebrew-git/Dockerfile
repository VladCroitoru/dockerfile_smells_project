FROM alpine
RUN apk add --no-cache openssh-client \
    && apk add --no-cache git
LABEL io.whalebrew.name git 
LABEL io.whalebrew.config.volumes '["~/:/root/"]'
ENTRYPOINT ["git"]

# Why mount everything?
# Many tools used to edit files including vi and sed --in-place may result in an inode change. Since Docker v1.1.0, this will produce an error such as “sed: cannot rename ./sedKdJ9Dy: Device or resource busy”. In the case where you want to edit the mounted file, it is often easiest to instead mount the parent directory.
# https://docs.docker.com/engine/tutorials/dockervolumes/#/mount-a-host-file-as-a-data-volume
# ubuntu@ip-172-31-45-76:~/whalebrew$ sudo git config --global user.email "iam@yourfather.com"
# error: could not write config file /root/.gitconfig: Resource busy
#LABEL io.whalebrew.config.volumes '["~/.gitconfig:/root/.gitconfig", "~/.ssh:/root/.ssh"]'
