# This docker file contains build environment
FROM opensuse/tumbleweed
MAINTAINER krytin <krytin.vitaly@apriorit.com>

RUN zypper -n update && zypper clean --all
RUN zypper -n install -t pattern devel_C_C++
RUN zypper -n install clang llvm-clang-devel llvm-devel cmake libelf-devel \
kernel-vanilla-devel kernel kernel-devel

RUN zypper -n dup

RUN zypper -n --no-gpg-checks install --oldpackage \
http://mirror.linux-ia64.org/opensuse/repositories/home:/dsterba:/kernel:/v4.10/openSUSE_Tumbleweed/x86_64/kernel-default-devel-4.10.17-1.1.x86_64.rpm \
http://mirror.linux-ia64.org/opensuse/repositories/home:/dsterba:/kernel:/v4.10/openSUSE_Tumbleweed/x86_64/kernel-default-4.10.17-1.1.x86_64.rpm \
http://mirror.linux-ia64.org/opensuse/repositories/home:/dsterba:/kernel:/v4.10/openSUSE_Tumbleweed/noarch/kernel-devel-4.10.17-1.1.noarch.rpm

RUN zypper -n --no-gpg-checks install --oldpackage \
http://mirror.linux-ia64.org/opensuse/repositories/home:/dsterba:/kernel:/v4.12/openSUSE_Tumbleweed/x86_64/kernel-default-devel-4.12.14-1.1.x86_64.rpm \
http://mirror.linux-ia64.org/opensuse/repositories/home:/dsterba:/kernel:/v4.12/openSUSE_Tumbleweed/x86_64/kernel-default-4.12.14-1.1.x86_64.rpm \
http://mirror.linux-ia64.org/opensuse/repositories/home:/dsterba:/kernel:/v4.12/openSUSE_Tumbleweed/noarch/kernel-devel-4.12.14-1.1.noarch.rpm

RUN zypper -n --no-gpg-checks install --oldpackage \
http://mirror.linux-ia64.org/opensuse/repositories/home:/dsterba:/kernel:/v4.15/openSUSE_Tumbleweed/x86_64/kernel-default-devel-4.15.12-1.1.x86_64.rpm \
http://mirror.linux-ia64.org/opensuse/repositories/home:/dsterba:/kernel:/v4.15/openSUSE_Tumbleweed/x86_64/kernel-default-4.15.12-1.1.x86_64.rpm \
http://mirror.linux-ia64.org/opensuse/repositories/home:/dsterba:/kernel:/v4.15/openSUSE_Tumbleweed/noarch/kernel-devel-4.15.12-1.1.noarch.rpm
