#!/usr/bin/python3
"""2-do_deploy_web_static module"""

from fabric.api import env, put, run, local
from datetime import datetime
import os


# Define the web servers
env.hosts = [35.174.185.171, 54.160.109.229]


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    if not os.path.exists("versions"):
        os.makedirs("versions")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{timestamp}.tgz"

    print(f"Packing web_static to {archive_name}")
    result = local(f"tar -cvzf {archive_name} web_static", capture=True)

    if result.succeeded:
        return archive_name
    return None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.
    """
    if not os.path.exists(archive_path):
        return False

    archive_filename = os.path.basename(archive_path)
    archive_name_no_ext = archive_filename.split('.')[0]
    release_path = f"/data/web_static/releases/{archive_name_no_ext}"

    try:
        # Upload the archive to /tmp/
        put(archive_path, "/tmp/")

        # Create release directory and uncompress the archive
        run(f"mkdir -p {release_path}")
        run(f"tar -xzf /tmp/{archive_filename} -C {release_path}")
        run(f"rm /tmp/{archive_filename}")
        run(f"mv {release_path}/web_static/* {release_path}/")
        run(f"rm -rf {release_path}/web_static")

        # Remove the existing symbolic link
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run(f"ln -s {release_path} /data/web_static/current")

        return True
    except Exception as e:
        return False
