from ddrown/android-cross-compile

maintainer Dan Drown <dan@drown.org>

run yum -y install gcc-c++
run git clone https://github.com/ddrown/irssiconnectbot-ncurses.git /home/admin/ncurses-5.9
run git clone https://github.com/ddrown/irssiconnectbot-protobuf.git /home/admin/protobuf-2.4.1
run git clone https://github.com/ddrown/openssl.git /home/admin/openssl
run git clone -b android-unicode https://github.com/ddrown/mosh.git /home/admin/mosh
add prebuild /home/admin/
run chmod 755 /home/admin/prebuild ; /home/admin/prebuild
run mkdir /target
add build /home/admin/
run chmod 755 /home/admin/build
cmd /home/admin/build
