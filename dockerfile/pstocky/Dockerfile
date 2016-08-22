FROM daocloud.io/python:2.7
MAINTAINER rtx3 <r@rtx3.com>>


RUN  apt-get update
# RUN apt-get ins
# RUN yum -y install epel-release
# RUN yum -y install python-devel python-pip python-setuptools git
# RUN yum -y update
# RUN yum -y install mysql-devel zlib-devel bzip2-devel sqlite-devel
# RUN yum -y install ibjpeg libjpeg-devel freetype freetype-devel zlib zlib-devel littlecms littlecms-devel libwebp libwebp-devel libfreetype libfreetype-devel gcc

# python packages
RUN pip install --upgrade pip -i http://pypi.douban.com/simple
RUN pip install  -i http://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.mirrors.ustc.edu.cn  django==1.8
RUN pip install -i http://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.mirrors.ustc.edu.cn django-grappelli==2.7.1 

RUN pip install -i http://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.mirrors.ustc.edu.cn djangorestframework==3.3.2 
# Markdown support for the browsable API. 
RUN pip install -i http://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.mirrors.ustc.edu.cn markdown==2.3.1 
RUN pip install -i http://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.mirrors.ustc.edu.cn django-filter==0.12.0 

# http://djangothumbnails.com/
RUN pip install -i http://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.mirrors.ustc.edu.cn django-thumbs==0.4

# http://django-extensions-zh.readthedocs.io/
RUN pip install -i http://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.mirrors.ustc.edu.cn django-extensions==1.6.7 

RUN pip install -i http://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.mirrors.ustc.edu.cn requests==2.10.0 

RUN pip install -i http://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.mirrors.ustc.edu.cn redis==2.10.5
RUN pip install -i http://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.mirrors.ustc.edu.cn django-redis==4.2.0 
RUN pip install -i http://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.mirrors.ustc.edu.cn MySQL-python==1.2.5

RUN pip install -i http://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.mirrors.ustc.edu.cn uWSGI==2.0.13


RUN cd /opt && \
    git clone https://github.com/pstocky/pstocky.git

RUN cd /opt/pstocky && \
    pip install -r backend/requirements.txt -i http://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.mirrors.ustc.edu.cn


EXPOSE 8000
WORKDIR /opt/pstocky/backend

RUN sh /opt/pstocky/backend/install.sh
RUN  echo "from django.contrib.auth import get_user_model;User = get_user_model(); User.objects.create_superuser('docker', '123')" | python manage.py shell
CMD ["python","/opt/pstocky/backend/manage.py","runserver","0.0.0.0:8000"]
