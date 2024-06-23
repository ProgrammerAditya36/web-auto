#!/usr/bin/env python3
import os
import sys

def create_fe_project(project_name):
    os.system(f"mkdir {project_name}")
    os.chdir(project_name)
    with open("index.html", "w") as f:
        f.write("<!DOCTYPE html>\n<html>\n<head>\n<title></title>\n<link rel='stylesheet' href='style.css'>\n</head>\n<body>\n<script src='script.js'></script>\n</body>\n</html>")
    os.system("touch style.css")
    os.system("touch script.js")
    os.system("code .")

def create_django_project(project_name, app_name=None):
    ret = os.system(f"django-admin startproject {project_name}")
    if ret == 0:
        print("Project created successfully")
        os.chdir(project_name)
        if app_name:
            os.system(f"python manage.py startapp {app_name}")
        os.system("code .")
    else:
        print("Error in creating project")
        c = int(input("Do you want to try again?\n1.Yes\n2.No\n"))
        if c == 2:
            sys.exit()

def create_react_project(project_name):
    os.system(f"npm create vite@latest {project_name} -- --template react")
    os.chdir(project_name)
    os.system
    os.system("code .")

def create_node_project(project_name):
    os.system(f"mkdir {project_name}")
    os.chdir(project_name)
    os.system("npm init -y")
    os.system("npm install express")
    with open("index.js", "w") as f:
        f.write("""const express = require('express')
const app = express()
app.get('/', (req, res) => {
    res.send('Hello World!')
})
app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000')
})""")
    os.system("code .")

def main():
    path = os.getcwd()
    while True:
        args = sys.argv[1:]
        if not args:
            print("Please provide project type and name")
            sys.exit(1)
        project = args[0]
        project_name = args[1] if len(args) > 1 else ""
        if project in ["1", "fe"]:
            project_name = project_name if project_name else "mywebapp"
            create_fe_project(project_name)
            break
        elif project in ["2", "django"]:
            project_name = project_name if project_name else "mydjangoapp"
            app_name = args[2] if len(args) > 2 else None
            create_django_project(project_name, app_name)
            break
        elif project in ["3", "react"]:
            project_name = project_name if project_name else "my-react-app"
            create_react_project(project_name)
            break
        elif project in ["4", "node"]:
            project_name = project_name if project_name else "my-node-app"
            create_node_project(project_name)
            break
        elif project == "5":
            break
        else:
            print("Invalid choice")
            continue

if __name__ == "__main__":
    main()
