FROM electronuserland/electron-builder

RUN apt update
RUN apt install --no-install-recommends -y software-properties-common
RUN add-apt-repository ppa:alexlarsson/flatpak
RUN apt update
RUN apt remove -y software-properties-common
RUN apt install --no-install-recommends -y flatpak flatpak-builder
RUN apt clean
RUN rm -rf /var/lib/apt/lists/*
RUN yarn global add bower gulp
RUN flatpak remote-add --no-gpg-verify --if-not-exists gnome https://sdk.gnome.org/gnome.flatpakrepo ; flatpak install -y gnome org.freedesktop.Sdk/x86_64/1.6
RUN flatpak install -y gnome org.freedesktop.Platform/x86_64/1.6
RUN flatpak install -y gnome org.freedesktop.Sdk/x86_64/1.4
RUN flatpak install -y --from https://s3-us-west-2.amazonaws.com/electron-flatpak.endlessm.com/electron-base-app-master.flatpakref || true

WORKDIR /project

CMD bash
