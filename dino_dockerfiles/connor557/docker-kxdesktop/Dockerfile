FROM connor557/ubuntu-xrdp-base

MAINTAINER cobrien@connorcrew.us.to

# set new password
RUN echo "root:Docker" | chpasswd

# install required tools
RUN apt-get update \
    && apt-get install --yes --force-yes --no-install-recommends software-properties-common \
        xorg \
        xserver-xorg \
        lightdm \
        lightdm-gtk-greeter \
        gnome-themes-standard \
        gtk2-engines-pixbuf \
        file-roller \
        evince \
        gpicview \
        leafpad \
        xfce4-whiskermenu-plugin \
        ttf-ubuntu-font-family \
        xfce4-goodies \
        thunderbird \
        firefox \
        pidgin \
    && add-apt-repository -y ppa:numix/ppa \
    && apt-get update \
    && apt-get install --yes --force-yes --no-install-recommends numix-icon-theme numix-icon-theme-circle \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# add the customised files
ADD ubuntu-files/lightdm-gtk-greeter.conf /etc/lightdm/lightdm-gtk-greeter.conf
ADD ubuntu-files/Adwaita-Xfce /usr/share/themes/Adwaita-Xfce
ADD ubuntu-files/xfce-perchannel-xml /etc/xdg/xfce4/xfconf/xfce-perchannel-xml
RUN mkdir -p /usr/share/backgrounds
ADD ubuntu-files/background-default.png /usr/share/backgrounds/background-default.png
RUN ln -s /usr/share/icons/Numix-Circle /usr/share/icons/KXicons
