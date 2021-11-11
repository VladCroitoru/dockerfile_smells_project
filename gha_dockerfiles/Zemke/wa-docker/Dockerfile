FROM ubuntu:18.04 AS builder

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  ca-certificates \
  wget \
  p7zip-full \
  unshield

COPY wa.iso .

# CD contents
RUN mkdir -p wa/cd \
  && cd wa/cd \
  && 7z x ../../wa.iso

# Game installation directory
RUN mkdir wa/cab \
  && cd wa/cab \
  && unshield x ../cd/Install/data1.cab

# Merge and fix case
RUN mv wa/cab/Program_Executable_Files wa/game \
  && cp -lnTR wa/cd/Data wa/game/DATA \
  && bash -c 'mv wa/game/User/{g,G}raves' \
  && bash -c 'mv wa/game/{g,G}raphics' \
  && bash -c 'mv wa/game/Graphics/{optionsmenu,OptionsMenu}'

RUN wget -nc https://dl.winehq.org/wine-builds/winehq.key -O /tmp/winehq.key

# Updates
COPY wa_3_8_gog_update.exe wa/game
COPY wa_3_8_1_cd_update.exe wa/game

# Installing the updates
RUN cd wa/game \
  && 7z x -aoa wa_3_8_gog_update.exe \
  && rm -rf \$PLUGINSDIR \
  && 7z x -aoa wa_3_8_1_cd_update.exe \
  && rm -rf \$PLUGINSDIR \
  && bash -c "printf '\x02' | dd of='WA.exe' bs=1 seek=2717442 count=1 conv=notrunc" \
  && bash -c "printf '\xF2' | dd of='WA.exe' bs=1 seek=360 count=1 conv=notrunc"

# Remove files unnecessary for non-interactive (headless) use
# RUN cd wa/game \
#   && find -regextype egrep -not -regex '^\.(|/(WA\.exe|ltfil10N\.DLL|ltkrn10N\.dll|lflmb10N\.dll|DATA(|/ImgHoles.*|/User(|/Languages(|/[0-9][^/]*(|/English.txt)))|/Mission.*|/Level.*|/Image.*|/Gfx(|/Gfx\.dir|/Water\.dir)|/Custom.*)))$' \
#     -printf 'Deleting %p\n' -delete


FROM ubuntu:18.04

# Get key to Wine repo
COPY --from=builder /tmp/winehq.key /tmp/winehq.key

# Add Wine repo
RUN apt-get update \
  && apt-get install -y software-properties-common gnupg \
  && apt-key add /tmp/winehq.key \
  && add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ bionic main' \
  && rm /tmp/winehq.key

# AMD 32-bit deps for Wine
RUN dpkg --add-architecture i386 \
  && add-apt-repository ppa:cybermax-dexter/sdl2-backport \
  && apt-get update \
  && apt-get install -y --install-recommends winehq-stable wine32 xvfb \
  && rm -rf /var/lib/apt/lists/*

# Create WINEPREFIX
RUN WINEDLLOVERRIDES="mscoree,mshtml=" xvfb-run wineboot -i \
  && wineserver -k

# Copy game installation directory
COPY --from=builder wa/game /root/.wine/drive_c/WA

# Suppress Wine compatibility warning (only needed for 3.8 and earlier)
RUN wine reg add 'HKEY_CURRENT_USER\Software\Team17SoftwareLTD\WormsArmageddon\Options' /v WineCompatibilitySuggested /t REG_DWORD /d 0x7FFFFFFF \
  && wineserver -k

# Add scripts
COPY scripts/* /usr/local/bin/

