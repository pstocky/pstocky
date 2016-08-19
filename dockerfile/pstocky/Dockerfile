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


EXPOSE 8000
WORKDIR /opt/pstocky/backend

RUN sh /opt/pstocky/backend/install.sh
RUN  echo "from django.contrib.auth import get_user_model;User = get_user_model(); User.objects.create_superuser('docker', '123')" | python manage.py shell
CMD ["/usr/bin/python","/opt/pstocky/backend/manage.py","runserver","0.0.0.0:8000"]
