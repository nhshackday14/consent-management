from fabric.api import env, lcd, run, local
from fabric.contrib.project import rsync_project
from fabric.contrib.files import sed
from fabric.context_managers import cd
env.key_filename = "../../nother.pem"
env.hosts = ["54.247.69.211"]
env.user = "ubuntu"


def rsync_to_prod():
    rsync_settings = {"remote_dir": "/home/ubuntu"}
    rsync_settings["delete"] = True
    rsync_settings["exclude"] = ["*.pyc", "*.git", "fabfile.py", "*.pdf", "db.sqlite3"]
    rsync_project(**rsync_settings)


def install_bower():
    with cd("consent-management"):
        run("npm install")
        run("bower install")
        with cd("consent-management"):
            sed("settings.py", "DEBUG = True", "DEBUG = False")


def collect_static():
    with lcd("consent_management"):
        local("python manage.py collectstatic")


def push_to_prod():
    collect_static()
    rsync_to_prod()
    install_bower()
