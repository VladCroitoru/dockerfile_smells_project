FROM opensuse:42.2

# Install build-deps (source-install is way overkill here, oh well)
RUN zypper addrepo obs://windows:mingw:win32/openSUSE_42.2 mingw32
RUN zypper addrepo obs://Emulators/openSUSE_Leap_42.2 Emulators
# wine depends on samba which depends on krb5 which conflicts with krb5-mini
RUN zypper -n --gpg-auto-import-keys install git make flex tar curl wine -krb5-mini dejagnu
RUN zypper -n source-install -d mingw32-cross-gcc-c++

# Download sources
RUN mkdir -p /opt/gcc49/build /opt/gcc5/build /opt/gcc6/build /opt/gcc6-patched/build && \
    git clone git://github.com/gcc-mirror/gcc -b gcc-4_9-branch /opt/gccsrc && \
    cd /opt/gcc49/build && \
    /opt/gccsrc/configure --prefix=/opt/gcc49/usr \
    --target=i686-w64-mingw32 --enable-languages="c,c++,fortran,lto,objc,obj-c++" \
    --disable-multilib --enable-threads=posix \
    --with-sysroot=/usr/i686-w64-mingw32/sys-root \
    --with-as=/usr/bin/i686-w64-mingw32-as && \
    make -j`nproc` && make install && cd .. && rm -rf build && \
    cd /opt/gccsrc && git checkout gcc-5-branch && \
    cd /opt/gcc5/build && \
    /opt/gccsrc/configure --prefix=/opt/gcc5/usr \
    --target=i686-w64-mingw32 --enable-languages="c,c++,fortran,lto,objc,obj-c++" \
    --disable-multilib --enable-threads=posix \
    --with-sysroot=/usr/i686-w64-mingw32/sys-root \
    --with-as=/usr/bin/i686-w64-mingw32-as && \
    make -j`nproc` && make install && cd .. && rm -rf build && \
    cd /opt/gccsrc && git checkout gcc-6-branch && \
    cd /opt/gcc6/build && \
    /opt/gccsrc/configure --prefix=/opt/gcc6/usr \
    --target=i686-w64-mingw32 --enable-languages="c,c++,fortran,lto,objc,obj-c++" \
    --disable-multilib --enable-threads=posix \
    --with-sysroot=/usr/i686-w64-mingw32/sys-root \
    --with-as=/usr/bin/i686-w64-mingw32-as && \
    make -j`nproc` && make install && cd .. && rm -rf build && \
    cd /opt/gccsrc && curl https://gist.githubusercontent.com/anonymous/4621fc4aba09827c7bde0e8acb9d2a88/raw/- | git apply -C2 && \
    rm -rf .git && \
    cd /opt/gcc6-patched/build && \
    /opt/gccsrc/configure --prefix=/opt/gcc6-patched/usr \
    --target=i686-w64-mingw32 --enable-languages="c,c++,fortran,lto,objc,obj-c++" \
    --disable-multilib --enable-threads=posix \
    --with-sysroot=/usr/i686-w64-mingw32/sys-root \
    --with-as=/usr/bin/i686-w64-mingw32-as && \
    make -j`nproc` && make install && cd .. && rm -rf build && \
    rm -rf /opt/gccsrc

RUN zypper -n install which patch cmake && \
    git clone git://github.com/JuliaLang/julia /opt/julia -b release-0.5 && \
    cd /opt/julia && mkdir -p usr/bin usr/tools && \
    cp /usr/i686-w64-mingw32/sys-root/mingw/bin/lib*.dll usr/bin && \
    cp /usr/i686-w64-mingw32/sys-root/mingw/bin/lib*.dll usr/tools && \
    echo 'XC_HOST = i686-w64-mingw32' > Make.user && \
    echo 'override MARCH = pentium4' >> Make.user

WORKDIR /opt/julia

RUN export PATH=/opt/gcc6/usr/bin:$PATH && \
    for i in `seq 5`; do make -j`nproc` -C deps \
    RCFLAGS="-I/usr/i686-w64-mingw32/sys-root/mingw/include -D_WIN32"; done
RUN echo $PATH
#    cp /opt/gcc$gccver/usr/i686-w64-mingw32/lib/*.dll Release+Asserts/bin && \
