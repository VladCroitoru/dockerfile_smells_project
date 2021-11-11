# 使用安装了最少的软件的镜像，也有使用 ruby:alpine
FROM ruby:2.3.3-slim

# Ruby 使用的是 Debian 系统
# 刷新 debian 的软件管理源，否则，慢得让人抓狂
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak && \
    echo "deb http://mirrors.163.com/debian/ jessie main non-free contrib" >/etc/apt/sources.list && \
    echo "deb http://mirrors.163.com/debian/ jessie-proposed-updates main non-free contrib" >>/etc/apt/sources.list && \
    echo "deb-src http://mirrors.163.com/debian/ jessie main non-free contrib" >>/etc/apt/sources.list && \
   echo "deb-src http://mirrors.163.com/debian/ jessie-proposed-updates main non-free contrib" >>/etc/apt/sources.list

# 安装必要套件
RUN apt-get update -qq && apt-get install -y build-essential mysql-common mysql-client libmysqlclient-dev

# 安装 mysql 
#RUN apt-get install -y mysql-server 
# 安装 sqlite3，这个用于test,development
RUN apt-get install -y libsqlite3-dev

# 安装 JS runtime，一定要装
RUN apt-get install -y nodejs

# 用于图片上传
RUN apt-get install -y imagemagick
RUN apt-get install -y libmagickwand-dev 

# 方便进到容器编辑、查看代码
RUN apt-get install -y vim

# 设置环境变量，即在后面可以用 $RAILS_ROOT
# 来指代容器中的 rails 程序放的目录
ENV RAILS_ROOT /var/www/tax

# 创建 rails 程序目录和程序运行所需要的 pids 的目录
RUN mkdir -p $RAILS_ROOT/tmp/pids

# 设置容器里的工作目录
WORKDIR $RAILS_ROOT

# 备份 Gemfile 及 lock到容器的工作目录中
# 当Gemfile 没有改变时，省略下面的 bundle install
COPY Gemfile Gemfile
COPY Gemfile.lock Gemfile.lock

# 安装 Rails 环境
RUN gem install bundler
RUN bundle install

RUN gem install passenger

# 将 Dockerfile 目录下所有内容复制到容器工作目录
COPY . .

# 比较重要的一步，对静态资源进行 precompile
#RUN bundle exec rake RAILS_ENV=$RAILS_ENV DATABASE_URL=mysql2://$MYSQL_USER:$MYSQL_PASSWORD@127.0.0.1/$MYSQL_DATABASE assets:precompile
#RUN RAILS_ENV=$RAILS_ENV bundle exec rake assets:precompile  --trace

# 当容器启动时运行的脚本，即 unicorn
#CMD ["config/containers/app_cmd.sh"]
