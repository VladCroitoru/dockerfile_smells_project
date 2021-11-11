FROM archlinux/base
RUN sed -i /\\[multilib\\]/,+1s/#// /etc/pacman.conf
RUN echo -e '[archlinuxcn]\nServer = https://cdn.repo.archlinuxcn.org/$arch' >> /etc/pacman.conf
RUN pacman-key --init
ADD package_list .
RUN pacman -Syu --noconfirm grep awk gettext archlinuxcn-keyring && \
      xprotodeps=$(pactree -sru xproto | sort) && \
      bash -c "indb=\$(comm -12 <(sort package_list) <(pacman -Slq | sort)) && \
      pkglist=\$(comm -23 <(echo \"\$indb\") <(echo \"$xprotodeps\"))$'\n'\$(comm -12 <(echo \"\$indb\") <(echo \"$xprotodeps\") | tail -n 100 | head -n 50 | while read pkg; do pactree -sl \$pkg | grep -q '^xproto$' || echo \$pkg; done) && \
      comm -23 <(echo \"\$pkglist\") <(echo \"\$pkglist\" | pacman -Fyl - | grep 'usr/share/applications/.*\.desktop$' | cut -d \  -f 1 | uniq | LANGUAGE=en_US.UTF-8 pacman -Si - | grep '^Name\|^Installed Size.*MiB$' | grep -B 1 '^Installed Size.*MiB$' | grep -v '\-\-' | tr '\n' '\t' | xargs -n 8 echo | awk '{print \$7,\$3}' | cat - <(echo 32) | sort -h | sed '1,/^32$/d' | cut -d \  -f 2 | sort)" | sed '/^linux$\|^linux-headers$/d'| pacman -S --needed --noconfirm - && \
      rm -rf /var/cache/pacman/pkg/*
      #RUN bash -c "pip install -r <(cut -d = -f 1 pip_package_list) --user"
      ADD .zshrc .base.vimrc .vimrc /root/
