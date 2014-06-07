from fabric.api import env, lcd, run, local
from fabric.contrib.project import rsync_project
from fabric.context_managers import cd, prefix
from fabric.operations import put
env.key_filename = "../../nother.pem"
env.hosts = ["54.247.69.211"]
env.user = "ubuntu"
app_name = "consent-management"


def rsync_to_prod():
    rsync_settings = {"remote_dir": "/home/ubuntu"}
    rsync_settings["delete"] = True
    rsync_settings["exclude"] = ["*.pyc", "*.git",
                                 "fabfile.py", "*.pdf", "db.sqlite3"]
    rsync_project(**rsync_settings)


def build_static():
    with cd("consent-management"):
        local("npm install")
        local("bower install")
        local("grunt")


def upload_settings():
    put(
        remote_path='consent-management/consent_management/consent_management',
        local_path="../server_settings.py"
    )


def workon():
        return "source /usr/local/bin/virtualenvwrapper.sh && workon %s" % app_name


def install_requirements():
    with prefix(workon()):
        with cd("consent-management"):
            run("pip install -r requirements.txt")


def collect_static():
    with lcd("consent_management"):
        local("python manage.py collectstatic --noinput")


def sync_db():
    with prefix(workon()):
        with cd("consent-management/consent_management"):
            run("./manage.py syncdb")
            run("./manage.py migrate")


def db_dump():
    with prefix(workon()):
        with cd("consent-management/consent_management"):
            run("./manage.py dumpdata > ../datadump.json")

def push_to_prod():
    build_static()
    collect_static()
    rsync_to_prod()
    db_dump()
    install_requirements()
    sync_db()
    upload_settings()
