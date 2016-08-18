FROM centos:centos7
MAINTAINER rtx3 <r@rtx3.com>>

RUN yum -y install epel-release
RUN yum -y install python-devel python-pip python-setuptools git
RUN yum -y update
RUN yum -y install mysql-devel zlib-devel bzip2-devel sqlite-devel
RUN yum -y install ibjpeg libjpeg-devel freetype freetype-devel zlib zlib-devel littlecms littlecms-devel libwebp libwebp-devel libfreetype libfreetype-devel gcc

RUN cd /opt && \
    git clone https://github.com/pstocky/pstocky.git

RUN cd /opt/pstocky && \
    pip install -r backend/requirements.txt

RUN chmod 777 /opt/pstocky/backend/base/settings.py

ADD ./local_settings.docker /opt/pstocky/backend/base/settings.py

EXPOSE 8000
WORKDIR /opt/pstocky

CMD ["/usr/bin/python","/opt/pstocky/backend/manage.py","runserver","0.0.0.0:8000"]
