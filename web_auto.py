#!/usr/bin/env python3
import os
import sys

def create_fe_project(projectname):
    os.makedirs(projectname, exist_ok=True)
    os.chdir(projectname)
    with open("index.html", "w") as f:
        f.write("<!DOCTYPE html>\n<html>\n<head>\n<title></title>\n<link rel='stylesheet' href='style.css'>\n</head>\n<body>\n<script src='script.js'></script>\n</body>\n</html>")
    open("style.css", 'a').close()
    open("script.js", 'a').close()
    os.system("code .")

def create_django_project(projectname, appname=None):
    ret = os.system(f"django-admin startproject {projectname}")
    if ret == 0:
        print("Project created successfully")
        os.chdir(projectname)
        if appname:
            os.system(f"python manage.py startapp {appname}")
        os.system("code .")
    else:
        print("Error in creating project")
        c = input("Do you want to try again? (y/n): ")
        if c.lower() != 'y':
            sys.exit()

def create_react_project(projectname):
    os.system(f"npm create vite@latest {projectname} -- --template react")
    os.chdir(projectname)
    os.system("npm install")
    os.system("code .")

def create_node_project(projectname):
    os.makedirs(projectname, exist_ok=True)
    os.chdir(projectname)
    os.system("npm init -y")
    os.system("npm install express")
    with open("index.js", "w") as f:
        f.write("const express = require('express')\nconst app = express()\napp.get('/', (req, res) => {\nres.send('Hello World!')\n})\napp.listen(3000, () => {\nconsole.log('Server is running on http://localhost:3000')\n})")
    os.system("code .")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: script.py <project_type> [project_name] [app_name]")
        sys.exit(1)

    project = sys.argv[1]
    projectname = sys.argv[2] if len(sys.argv) > 2 else None
    appname = sys.argv[3] if len(sys.argv) > 3 else None

    if project in ["1", "fe"]:
        if not projectname:
            projectname = "mywebapp"
        create_fe_project(projectname)
    elif project in ["2", "django"]:
        if not projectname:
            projectname = "mydjangoapp"
        create_django_project(projectname, appname)
    elif project in ["3", "react"]:
        if not projectname:
            projectname = "my-react-app"
        create_react_project(projectname)
    elif project in ["4", "node"]:
        if not projectname:
            projectname = "my-node-app"
        create_node_project(projectname)
    elif project == "5":
        sys.exit()
    else:
        print("Invalid choice")
        sys.exit(1)
