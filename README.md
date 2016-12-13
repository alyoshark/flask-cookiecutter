# My Simple Flask Cookiecutter Template

Yet another standard cookiecutter template for web, with a focus on scafolding a minimal
site using Flask that can be extended of modules using blueprints.

```
./myawesomesite.com <---------- main directory is mostly for SA's use
├── Dockerfile
├── README.md
├── api <---------------------- API Flask app
│   ├── config.py <------------ WSGI app config
│   ├── run.ini <-------------- uWSGI ini file
│   ├── views <---------------- all the modules
│   │   ├── __init__.py
│   │   └── root <------------- root blueprint, registered in /
│   │       └── __init__.py <-- blueprint instance, bp, under __init__
│   └── wsgi.py
├── docker-compose.yml
├── frontend <----------------- Frontend stuff
│   └── index.html
├── nginx-site.conf <---------- Nginx config
├── requirements.txt
└── start.sh
```
