FROM registry.gitlab.gnome.org/gnome/gnome-runtime-images/gnome:3.34
RUN flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
RUN flatpak install --noninteractive -y flathub org.freedesktop.Sdk.Extension.rust-nightly//19.08
