#!/usr/bin/env python3
import os
import sys

def create_fe_project(projectname, current_folder=False):
    if not current_folder:
        os.makedirs(projectname, exist_ok=True)
        os.chdir(projectname)
    with open("index.html", "w") as f:
        f.write("<!DOCTYPE html>\n<html>\n<head>\n<title></title>\n<link rel='stylesheet' href='style.css'>\n</head>\n<body>\n<script src='script.js'></script>\n</body>\n</html>")
    open("style.css", 'a').close()
    open("script.js", 'a').close()
    os.system("code .")

def create_django_project(projectname, appname=None, current_folder=False):
    if not current_folder:
        ret = os.system(f"django-admin startproject {projectname}")
        if ret != 0:
            print("Error in creating project")
            c = input("Do you want to try again? (y/n): ")
            if c.lower() != 'y':
                sys.exit()
            return
        os.chdir(projectname)
    if appname:
        os.system(f"python manage.py startapp {appname}")
    os.system("code .")

def create_react_project(projectname, current_folder=False):
    if not current_folder:
        os.system(f"npm create vite@latest {projectname} -- --template react")
        os.chdir(projectname)
    os.system("npm install")
    os.system("code .")

def create_node_project(projectname, current_folder=False):
    if not current_folder:
        os.makedirs(projectname, exist_ok=True)
        os.chdir(projectname)
    os.system("npm init -y")
    os.system("npm install express")
    with open("index.js", "w") as f:
        f.write("const express = require('express')\nconst app = express()\napp.get('/', (req, res) => {\nres.send('Hello World!')\n})\napp.listen(3000, () => {\nconsole.log('Server is running on http://localhost:3000')\n})")
    os.system("code .")

def start_environment(project):
    if project in ["1", "fe"]:
        print("Starting live server for Frontend project...")
        os.system("live-server")
    elif project in ["2", "django"]:
        print("Starting Django development server...")
        os.system("python manage.py runserver")
    elif project in ["3", "react"]:
        print("Starting React development server with all ports exposed...")
        os.environ["HOST"] = "0.0.0.0"
        os.system("npm run dev")
    elif project in ["4", "node"]:
        print("Starting Node.js server with nodemon...")
        os.system("nodemon index.js")  # Use nodemon to run Node.js server
    else:
        print("Invalid project type for starting environment")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: script.py <project_type> [project_name] [-cf | -start] [app_name]")
        sys.exit(1)

    project = sys.argv[1]
    projectname = None
    appname = None
    current_folder = False
    start_flag = False

    if "-cf" in sys.argv and "-start" in sys.argv:
        print("Error: Cannot use -cf and -start flags together")
        sys.exit(1)

    if "-cf" in sys.argv:
        current_folder = True
        projectname = os.path.basename(os.getcwd())
        sys.argv.remove("-cf")
    elif "-start" in sys.argv:
        start_flag = True
        projectname = sys.argv[2] if len(sys.argv) > 2 else None
        sys.argv.remove("-start")
    else:
        projectname = sys.argv[2] if len(sys.argv) > 2 else None
        appname = sys.argv[3] if len(sys.argv) > 3 else None

    if project in ["1", "fe"]:
        if not projectname:
            projectname = "mywebapp"
        if start_flag:
            start_environment(project)
        else:
            create_fe_project(projectname, current_folder)
    elif project in ["2", "django"]:
        if not projectname:
            projectname = "mydjangoapp"
        if start_flag:
            start_environment(project)
        else:
            create_django_project(projectname, appname, current_folder)
    elif project in ["3", "react"]:
        if not projectname:
            projectname = "my-react-app"
        if start_flag:
            start_environment(project)
        else:
            create_react_project(projectname, current_folder)
    elif project in ["4", "node"]:
        if not projectname:
            projectname = "my-node-app"
        if start_flag:
            start_environment(project)
        else:
            create_node_project(projectname, current_folder)
    elif project == "5":
        sys.exit()
    else:
        print("Invalid choice")
        sys.exit(1)
