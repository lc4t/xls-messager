# xls-messager
xls-messager

### install
    yum install git wget vim

    cd /tmp
    wget -q http://peak.telecommunity.com/dist/ez_setup.py
    python ez_setup.py
    wget --no-check-certificate https://github.com/pypa/pip/archive/1.5.5.tar.gz
    tar zvxf 1.5.5.tar.gz
    cd pip-1.5.5/
    python setup.py install

    pip install virtualenv
    virtualenv messager(first time only)
    cd messager/
    source bin/activate(every time)
    git clone https://github.com/lc4t/xls-messager

    # django
    pip install django==1.7.1 celery django-compat html2text jsonfield premailer
        
    
    pip install ... (somethings missing)
    python manage.py makemigrations
    python manage.py migrate
    test run: python manage.py runserver

### run
    cd messager/
    source bin/activate(every time)
    see xls-messager/proj/Readme.md