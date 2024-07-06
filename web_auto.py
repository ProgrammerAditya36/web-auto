#!/usr/bin/env python33

import os
import sys
import json
import requests
from requests.auth import HTTPBasicAuth

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
        os.system(f"python3 manage.py startapp {appname}")
    os.system("code .")

def create_react_project(projectname, current_folder=False):
    if not current_folder:
        os.system(f"npm create vite@latest {projectname} -- --template react")
        os.chdir(projectname)
    
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

def check_repo_exists(username, repo_name, token):
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    response = requests.get(url, auth=HTTPBasicAuth(username, token))
    return response.status_code == 200

def create_repo(username, repo_name, token):
    url = "https://api.github.com/user/repos"
    data = {
        "name": repo_name,
        "private": False,  # Make the repository public
        "auto_init": True  # Initialize the repository with a README file
    }
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.post(url, auth=HTTPBasicAuth(username, token), headers=headers, json=data)
    return response.status_code == 201

def start_environment(project):
    if project in ["1", "fe"]:
        print("Starting live server for Frontend project...")
        os.system("live-server")
    elif project in ["2", "django"]:
        print("Starting Django development server...")
        os.system("python3 manage.py runserver")
    elif project in ["3", "react"]:
        print("Starting React development server with all ports exposed...")
        os.system("vite --host 0.0.0.0")
    elif project in ["4", "node"]:
        print("Starting Node.js server with nodemon...")        
        os.system("npm install -g nodemon")
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
    elif "-cc" in sys.argv:
        if "react" not in sys.argv:
            print("Error: -cc flag can only be used with react project")
            sys.exit(1)
        component_name = sys.argv[3] if len(sys.argv) > 3 else 'Component'
        if(os.path.exists("src") == False):
            print("Error: src folder not found ")
            sys.exit(1)
        os.chdir("src")
        os.makedirs("components", exist_ok=True)
        os.chdir("components")
        os.makedirs(component_name, exist_ok=True)
        os.chdir(component_name)
        with open(f"{component_name}.jsx", "w") as f:
            f.write(f"import React from 'react';\nimport './{component_name}.css'\nconst {component_name} = () => {{\nreturn (\n<div>\n<h1>{component_name}</h1>\n</div>\n)\n}}\n\nexport default {component_name};")
        open(f"{component_name}.css", 'a').close()
        sys.exit()
    elif "-mp" in sys.argv:
        if "react" not in sys.argv:
            print("Error: -mp flag can only be used with react project")
            sys.exit(1)
        page_name = sys.argv[3] if len(sys.argv) > 3 else 'Page'
        homepage = f"https://ProgrammerAditya36.github.io/{page_name}"
        username = "ProgrammerAditya36"
        repo_name = page_name
        token = os.getenv("GITHUB_TOKEN")
        if not token:
            print("Error: GitHub token not found. Set the GITHUB_TOKEN environment variable.")
            sys.exit(1)
        if not check_repo_exists(username, repo_name, token):
            print("Creating a new repository...")
            if not create_repo(username, repo_name, token):
                print("Error in creating repository")
                sys.exit(1)
            print("Repository created successfully")
        else:
            print("Repository already exists")
        os.system("git init")
        os.system(f"git remote add origin https://github.com/{username}/{repo_name}.git")
        os.system("git add .")
        os.system("git commit -m 'Deploying to GitHub Pages'")
        os.system("git push -u origin main")

        os.system("npm run build")
        with open("vite.config.js", "r") as f:
            lines = f.readlines()
        insert_index = -1
        for i,line in enumerate(lines):
            if 'export default' in line:
                insert_index = i+1
                break
        base_config = " base:'./',\n"
        if insert_index != -1 and base_config not in lines:
            lines.insert(insert_index, base_config)
        with open("vite.config.js", "w") as f:
            f.writelines(lines)
        with open("package.json","r") as f:
            package_data = json.load(f)
        
        package_data["homepage"] = homepage
        package_data["scripts"]["predeploy"] = "npm run build"
        package_data["scripts"]["deploy"] = "gh-pages -d dist"
        with open("package.json","w") as f:
            json.dump(package_data,f,indent=2)
        
        os.system("npm run deploy")
        print(f"Deployment successful the page is live at {homepage}")
        sys.exit()

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
