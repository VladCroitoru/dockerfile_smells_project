FROM base/archlinux

MAINTAINER Sebastian Gutsche

RUN \
    echo "Server = http://ftp.halifax.rwth-aachen.de/archlinux/\$repo/os/\$arch" > /etc/pacman.d/mirrorlist && \
    pacman --noconfirm -Sy archlinux-keyring && \
    
    pacman --noconfirm -Syu alsa-lib\
    apache-ant\
    apr\
    apr-util\
    arch-install-scripts\
    atk\
    autoconf\
    automake\
    avahi\
    bash-completion\
    binutils\
    bison\
    boost\
    boost-libs\
    bridge-utils\
    btrfs-progs\
    ca-certificates-cacert\
    ca-certificates-mozilla\
    ca-certificates-utils\
    cairo\
    cgmanager\
    clang\
    cmake\
    compositeproto\
    conntrack-tools\
    cpupower\
    cryptsetup\
    damageproto\
    dbus-glib\
    desktop-file-utils\
    dnssec-anchors\
    dnsutils\
    elfutils\
    ethtool\
    fakeroot\
    fixesproto\
    flex\
    flint\
    fltk\
    fontconfig\
    fontsproto\
    freetype2\
    gc\
    gcc\
    gdk-pixbuf2\
    gf2x\
    giflib\
    git\
    glpk\
    glu\
    gnutls\
    gpm\
    graphite\
    groff\
    gtk-update-icon-cache\
    gtk2\
    guile\
    harfbuzz\
    hicolor-icon-theme\
    hwloc\
    icu\
    idnkit\
    imlib2\
    inputproto\
    irqbalance\
    jasper\
    java-environment-common\
    java-hamcrest\
    java-runtime-common\
    jdk8-openjdk\
    jfsutils\
    jre8-openjdk\
    jre8-openjdk-headless\
    js17\
    junit\
    kbproto\
    ldns\
    libaio\
    libatomic_ops\
    libcap-ng\
    libcroco\
    libcups\
    libdaemon\
    libdatrie\
    libdrm\
    libedit\
    libepoxy\
    libevdev\
    libevent\
    libexif\
    libfm\
    libfm-extra\
    libfontenc\
    libgssglue\
    libice\
    libid3tag\
    libidn\
    libjpeg-turbo\
    libkeybinder2\
    libmad\
    libmariadbclient\
    libmicrohttpd\
    libmnl\
    libmpc\
    libnetfilter_conntrack\
    libnetfilter_cthelper\
    libnetfilter_cttimeout\
    libnetfilter_queue\
    libnfnetlink\
    libnih\
    libnotify\
    libomxil-bellagio\
    libpciaccess\
    libpipeline\
    libpng\
    librpcsecgss\
    librsvg\
    libsm\
    libtasn1\
    libthai\
    libtiff\
    libtool\
    libtxc_dxtn\
    libunique\
    libwnck\
    libx11\
    libxau\
    libxcb\
    libxcomposite\
    libxcursor\
    libxdamage\
    libxdmcp\
    libxext\
    libxfixes\
    libxfont\
    libxft\
    libxi\
    libxinerama\
    libxkbfile\
    libxml-perl\
    libxml2\
    libxmu\
    libxrandr\
    libxrender\
    libxres\
    libxshmfence\
    libxslt\
    libxt\
    libxtst\
    libxxf86vm\
    libyaml\
    linux\
    linux-firmware\
    llvm\
    llvm-libs\
    lsof\
    ltrace\
    lua\
    lvm2\
    lxappearance\
    lxappearance-obconf\
    lxc\
    lxde-common\
    lxde-icon-theme\
    lxdm\
    lxinput\
    lxlauncher\
    lxmenu-data\
    lxmusic\
    lxpanel\
    lxrandr\
    lxsession\
    lxtask\
    lxterminal\
    lz4\
    lzo\
    m4\
    make\
    man-db\
    man-pages\
    mdadm\
    menu-cache\
    mesa\
    mesa-libgl\
    mkinitcpio\
    mkinitcpio-busybox\
    mtdev\
    munin-node\
    net-tools\
    nettle\
    nfs-utils\
    nfsidmap\
    npth\
    nspr\
    nss\
    ntp\
    numactl\
    openbox\
    openmpi\
    openslp\
    p11-kit\
    pango\
    patch\
    pciutils\
    pcmanfm\
    pcmciautils\
    perl-date-manip\
    perl-error\
    perl-fcgi\
    perl-file-copy-recursive\
    perl-html-template\
    perl-io-socket-inet6\
    perl-log-log4perl\
    perl-net-server\
    perl-socket6\
    perl-term-readline-gnu\
    perl-uri\
    perl-xml-libxml\
    perl-xml-libxslt\
    perl-xml-namespacesupport\
    perl-xml-parser\
    perl-xml-sax\
    perl-xml-sax-base\
    perl-xml-writer\
    pixman\
    pkg-config\
    polkit\
    postfix\
    postgresql-libs\
    python\
    python-pip\
    python2\
    randrproto\
    recordproto\
    reiserfsprogs\
    renderproto\
    rpcbind\
    rrdtool\
    rsync\
    ruby\
    rxvt-unicode\
    rxvt-unicode-terminfo\
    s-nail\
    screen\
    serf\
    shared-mime-info\
    smartmontools\
    sqlite\
    startup-notification\
    strace\
    subversion\
    sudo\
    syslinux\
    tcl\
    thin-provisioning-tools\
    tinycdb\
    ttf-dejavu\
    vim\
    vim-runtime\
    vte\
    vte-common\
    wayland\
    wget\
    xcb-proto\
    xcb-util\
    xdg-utils\
    xextproto\
    xf86-input-evdev\
    xf86vidmodeproto\
    xfsprogs\
    xineramaproto\
    xkeyboard-config\
    xmms2\
    mercurial\
    xproto && \
    
    pacman-db-upgrade && \
    useradd -d /home/homalg -m -s /bin/bash -c "standard user" -g users -G wheel homalg && \
    echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

USER homalg

# Singular from binaries
RUN    cd /tmp \
    && wget http://www.mathematik.uni-kl.de/ftp/pub/Math/Singular/UNIX/Singular-4-0-2-x86_64-Linux.tar.gz \
    && wget http://www.mathematik.uni-kl.de/ftp/pub/Math/Singular/UNIX/Singular-4-0-2-share.tar.gz \
    && cd /home/homalg \
    && mkdir install_singular \
    && cd install_singular \
    && gzip -dc /tmp/Singular-4-0-2-x86_64-Linux.tar.gz | tar -pxf - \
    && gzip -dc /tmp/Singular-4-0-2-share.tar.gz | tar -pxf - \
    && sudo ln -snf /home/homalg/install_singular/bin/Singular /usr/local/bin/Singular \
    && rm -rf /tmp/Singular*

RUN    cd /tmp \
    && wget http://www.gap-system.org/pub/gap/gap47/tar.gz/gap4r7p8_2015_06_09-20_27.tar.gz \
    && tar -xf gap*tar* \
    && rm -rf gap*tar* \
    && sudo mv gap4r7 /opt/ \
    && sudo chown -R homalg /opt/gap4r7 \
    && cd /opt/gap4r7 \
    && ./configure --with-gmp=system \
    && make -j \
    && cd pkg \
    && wget https://raw.githubusercontent.com/gap-system/gap-docker/master/InstPackages.sh \
    && chmod +x InstPackages.sh \
    && ./InstPackages.sh \
    && rm -rf InstPackages.sh \
    && cd /opt/gap4r7 \
    && mkdir local \
    && cd local \
    && mkdir pkg \
    && sudo bash -c "echo '#!/bin/sh' > /usr/bin/gap" \
    && sudo bash -c "echo '/opt/gap4r7/bin/gap.sh -l \"/opt/gap4r7/local;/opt/gap4r7\" \"\$@\"' >> /usr/bin/gap" \
    && sudo ln -snf /usr/bin/gap /usr/bin/gap.sh \
    && sudo chmod +x /usr/bin/gap \
    && mkdir /home/homalg/.gap \
    && echo 'SetUserPreference( "UseColorPrompt", true );' > /home/homalg/.gap/gap.ini \
    && echo 'SetUserPreference( "UseColorsInTerminal", true );' >> /home/homalg/.gap/gap.ini \
    && echo 'SetUserPreference( "HistoryMaxLines", 10000 );' >> /home/homalg/.gap/gap.ini \
    && echo 'SetUserPreference( "SaveAndRestoreHistory", true );' >> /home/homalg/.gap/gap.ini \
    && cd /opt/gap4r7/local/pkg \
    && export homalg_modules="AlgebraicThomas AbelianSystems alexander AutoDoc Blocks Conley D-Modules CAP_project \
                              k-Points LessGenerators LetterPlace SCO SCSCP_ForHomalg Sheaves SimplicialObjects \
                              SystemTheory VirtualCAS CombinatoricsForHomalg CAP PrimaryDecomposition SingularForHomalg homalg_project" \
    && for i in $homalg_modules; do git clone https://github.com/homalg-project/${i}.git; done

RUN sudo pip install jupyter

RUN    cd home/homalg \
    && git clone https://github.com/gap-system/jupyter-gap.git \
    && git clone https://github.com/sebasguts/jupyter-singular.git \
    && mkdir jupyterkernels \
    && cd jupyterkernels \
    && mv ../jupyter-gap/wrapper-kernel gap-wrapper-kernel \
    && mv ../jupyter-singular/wrapper-kernel singular-wrapper-kernel \
    && rm -rf /home/homalg/jupyter-gap \
    && rm -rf /home/homalg/jupyter-singular \
    && cd /home/homalg/jupyterkernels/gap-wrapper-kernel \
    && sudo python setup.py install \
    && sudo python -m jupyter_gap_wrapper.install

EXPOSE 8888

CMD /bin/bash -c "cd /home/homalg/jupyterkernels/singular-wrapper-kernel && sudo python -m singular_kernel.install && sudo ipython notebook --no-browser"
