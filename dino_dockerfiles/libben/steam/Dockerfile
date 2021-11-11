FROM vcatechnology/arch

ENV HOME /home/steam
ARG GRAPHICS_DRIVERS="xf86-video-nouveau mesa-libgl lib32-mesa-libgl"
ENV PULSE_SERVER unix:/tmp/pulse

RUN echo -e "[multilib]\nInclude = /etc/pacman.d/mirrorlist" >> /etc/pacman.conf

# Create user steam with access to video and audio devices
RUN useradd -m -g wheel -G video,audio -s /bin/bash steam

# the script called when you execute steam crashes without awk. It wants lspci,
# cmp, and xdg-user-dir, and says it wants to set the env to 'python'. But: we
# don't need xdg-user-dir, I think, because it manages home subfolders like
# ~/Music and we don't have any. Python's massive too, but I'm leaving it in.
# When I tried removing it, Steam wouldn't update at launch.
RUN pacman -Syu --noconfirm $GRAPHICS_DRIVERS sudo awk diffutils pciutils python pulseaudio steam

# set up sudo permissions for user steam
RUN echo 'steam ALL = NOPASSWD: ALL' > /etc/sudoers.d/steam
RUN chmod 0440 /etc/sudoers.d/steam

USER steam
# The 'share' folder must be a volume mounted from the host to persist all game
# data; it is the parent of steam and some Steam games create folders here.
VOLUME /home/steam/.local/share
ENTRYPOINT ["steam"]
