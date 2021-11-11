FROM samuelololol/docker-gentoo-crossdev-distccd
MAINTAINER samuelololol <samuelololol@gmail.com>
# remove to prevent crossdev build linux-headers fail
RUN rm /sbin/unix_chkpwd
#RUN FEATURES="${FEATURES} -ccache" crossdev -S -v -t armv6j-hardfloat-linux-gnueabi -s3 -P -uv
RUN FEATURES="${FEATURES} -ccache" crossdev -S -v -t armv6j-hardfloat-linux-gnueabi -s3
