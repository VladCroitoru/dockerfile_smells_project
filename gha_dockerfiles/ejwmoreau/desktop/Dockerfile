FROM archlinux/base

# Setup pacman and sudo
RUN pacman -Sy --noconfirm sudo

# Setup user
# Disabling for now because it would be tricky to get working. Problems unsolved:
# 1. Adding rothaq on the sudoers list
# 2. Passing the fake sudo password to scripts that need to run
#RUN useradd --create-home --shell /bin/bash rothaq
#RUN printf "rothaq\nrothaq" | passwd rothaq
#USER rothaq
#WORKDIR /home/rothaq/desktop
WORKDIR /home/root/desktop

# Setup Ansible and dependencies
COPY ./bin/setup.sh ./bin/setup.sh
RUN ./bin/setup.sh

# Copy all the scripts/repo content
COPY . .

CMD ansible-playbook --inventory-file '127.0.0.1,' --become linux.yaml
