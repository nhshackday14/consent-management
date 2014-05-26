from fabric.api import env
from fabric.contrib.project import rsync_project
from fabric.api import run
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


def push_to_prod():
    rsync_to_prod()
    install_bower()
