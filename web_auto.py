#!/usr/bin/env python3
import shutil
import sys
import os
import json
import requests
from requests.auth import HTTPBasicAuth
def create_redux():
    os.system("npm install redux react-redux @reduxjs/toolkit")
    os.makedirs("src/app", exist_ok=True)
    open("src/app/store.jsx", 'a').close()
    with open("src/main.jsx", "w") as f:
        f.write("""
                import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import { Provider } from "react-redux";
import { store } from "./app/store";
ReactDOM.createRoot(document.getElementById("root")).render(
    <React.StrictMode>
        <Provider store={store}>
            <App />
        </Provider>
    </React.StrictMode>,
);

                
                """)
        
def create_react_project(projectname, ts=False):
    template = "react-ts" if ts else "react"
    print(f"Creating a new React project with template {template}...")
    os.system(f"npm create vite@latest {projectname} -- --template {template}")
    os.chdir(projectname)
    tw = input("Do you want to use Tailwind CSS? (y/n): ")
    redux = input("Do you want to use Redux? (y/n): ")
    
    if tw.lower() == "y":
        setup_tailwind(react=True)
    if redux.lower() == "y":
        create_redux()
    os.system("npm install")
    start = input("Do you want to start the development server? (y/n): ")
    if start.lower() == "y":
        os.system("wa react -start")
    os.system("code .")
def setup_prettier():
    os.system("npm install -D prettier prettier-plugin-tailwindcss")
    with open(".prettierrc", "w") as f:
        f.write("""{ "plugins": ["prettier-plugin-tailwindcss"], "tabWidth": 4 }""")
    
    
        
def create_react_component(nodir=False, component_name='Component', create_css=False, ts=False, dir='components'):
    extension = "tsx" if ts else "jsx"
    if not os.path.exists("src"):
        print("Error: src folder not found")
        return

    os.chdir("src")
    os.makedirs(dir, exist_ok=True)
    os.chdir(dir)
    print(nodir)
    if( not nodir):
        os.makedirs(component_name, exist_ok=True)
        os.chdir(component_name)
        with open(f"{component_name}.{extension}", "w") as f:
            f.write(f"import React from 'react';\nimport './{component_name}.css'\nconst {component_name} = () => {{\nreturn (\n<div>\n<h1>{component_name}</h1>\n</div>\n)\n}}\n\nexport default {component_name};")
    if (create_css):
        os.makedirs(component_name, exist_ok=True)
        os.chdir(component_name)
        with open(f"{component_name}.{extension}", "w") as f:
            f.write(f"import React from 'react';\nimport './{component_name}.css'\nconst {component_name} = () => {{\nreturn (\n<div>\n<h1>{component_name}</h1>\n</div>\n)\n}}\n\nexport default {component_name};")
        open(f"{component_name}.css", 'a').close()
    else:
        with open(f"{component_name}.{extension}", "w") as f:
            f.write(f"import React from 'react';\nconst {component_name} = () => {{\nreturn (\n<div>\n<h1>{component_name}</h1>\n</div>\n)\n}}\n\nexport default {component_name};")
    
def deploy_react_project(page_name='Page', ts=False):
    home_link = os.getenv("HOMEPAGE")
    homepage = f"{home_link}{page_name}"
    username = os.getenv("USERNAME")
    repo_name = page_name
    token = os.getenv("GITHUB_TOKEN")

    if not token:
        print("Error: GitHub token not found. Set the GITHUB_TOKEN environment variable.")
        return

    if not check_repo_exists(username, repo_name, token):
        print("Creating a new repository...")
        if not create_repo(username, repo_name, token):
            print("Error in creating repository")
            return
        print("Repository created successfully")
        os.system("git init")
    else:
        print("Repository already exists")

    os.system(f"git remote add origin https://github.com/{username}/{repo_name}.git")
    os.system("npm install gh-pages --save-dev")

    os.system("npm run build")
    update_vite_config()
    update_package_json(homepage)
    os.system("npm run deploy")
    print(f"Deployment successful. The page is live at {homepage}")

def check_repo_exists(username, repo_name, token):
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    response = requests.get(url, auth=HTTPBasicAuth(username, token))
    return response.status_code == 200

def create_repo(username, repo_name, token):
    url = "https://api.github.com/user/repos"
    data = {
        "name": repo_name,
        "private": True,
        "auto_init": False
    }
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.post(url, auth=HTTPBasicAuth(username, token), headers=headers, json=data)
    return response.status_code == 201

def update_vite_config():
    with open("vite.config.js", "r") as f:
        lines = f.readlines()
    insert_index = -1
    for i, line in enumerate(lines):
        if 'export default' in line:
            insert_index = i + 1
            break
    base_config = " base:'./',\n"
    if insert_index != -1 and base_config not in lines:
        lines.insert(insert_index, base_config)
    with open("vite.config.js", "w") as f:
        f.writelines(lines)

def update_package_json(homepage):
    with open("package.json", "r") as f:
        package_data = json.load(f)
    package_data["homepage"] = homepage
    package_data["scripts"]["predeploy"] = "npm run build"
    package_data["scripts"]["deploy"] = "gh-pages -d dist"
    with open("package.json", "w") as f:
        json.dump(package_data, f, indent=2)

def create_node_project(projectname):
    os.makedirs(projectname, exist_ok=True)
    os.chdir(projectname)
    
    os.system("npm init -y")
    os.system("npm install express")
    
    with open("index.js", "w") as f:
        f.write(
            "const express = require('express')\n"
            "const app = express()\n"
            "app.get('/', (req, res) => {\n"
            "res.send('Hello World!')\n"
            "})\n"
            "app.listen(3000, () => {\n"
            "console.log('Server is running on http://localhost:3000')\n"
            "})"
        )
    
    os.system("code .")
def create_django_project(projectname="myproject", appname="myapp"):
    # Step 1: Create Django project
    ret = os.system(f"django-admin startproject {projectname}")
    if ret != 0:
        print("Error in creating project")
        return
    
    # Step 2: Navigate into the project directory
    os.chdir(projectname)
    
    # Step 3: Create Django app if specified
    if appname:
        os.system(f"python3 manage.py startapp {appname}")
    
    # Step 4: Create .vscode/settings.json for VS Code settings
    os.makedirs(".vscode", exist_ok=True)
    with open(".vscode/settings.json", "w") as f:
        f.write("""{
            "editor.formatOnSave": true,
            "files.associations": {"*.html": "django-html"}
        }""")
    
    # Step 5: Create static, media, and templates directories
    os.makedirs("static", exist_ok=True)
    os.makedirs("media", exist_ok=True)
    os.makedirs("templates", exist_ok=True)
    
    # Step 6: Write new settings.py
    settings_content = f"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'your-secret-key'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '{appname}',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '{projectname}.urls'

TEMPLATES = [
    {{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {{
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        }},
    }},
]

WSGI_APPLICATION = '{projectname}.wsgi.application'

DATABASES = {{
    'default': {{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }}
}}

AUTH_PASSWORD_VALIDATORS = [
    {{
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    }},
    {{
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    }},
    {{
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    }},
    {{
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    }},
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    """
    
    with open(f"{projectname}/settings.py", "w") as f:
        f.write(settings_content)
    
    # Step 7: Make initial migrations
    os.system("python3 manage.py makemigrations")
    os.system("python3 manage.py migrate")
    
    # Step 8: Open VS Code
    os.system("code .")

def create_fe_project(projectname):
    os.makedirs(projectname, exist_ok=True)
    os.chdir(projectname)
    
    with open("index.html", "w") as f:
        f.write("<!DOCTYPE html>\n<html>\n<head>\n<title></title>\n<link rel='stylesheet' href='style.css'>\n</head>\n<body>\n<script src='script.js'></script>\n</body>\n</html>")
    
    open("style.css", 'a').close()
    open("script.js", 'a').close()
    os.system("code .")

def start_project(project):
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
        print("Invalid project type for starting project")

def copy_hooks():
    hooks_dir = '/usr/local/bin/hooks'
    destination_dir = 'src/hooks'
    if not os.path.exists(hooks_dir):
        print("Error: hooks directory not found")
        return
    
    if not os.path.exists('src'):
        print("Error: src directory not found")
        return

    os.makedirs(destination_dir, exist_ok=True)
    
    for file_name in os.listdir(hooks_dir):
        full_file_name = os.path.join(hooks_dir, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, destination_dir)
    
    print("Hooks copied successfully")
def setup_tailwind(react=False, material_tailwind=False):
    os.system("npm install -D tailwindcss@latest postcss@latest autoprefixer@latest")
    os.system("npx tailwindcss init -p")
    
    tailwind_config = ""
    if material_tailwind:
        os.system("npm i @material-tailwind/react")
        tailwind_config = """
import withMT from '@material-tailwind/react/utils/withMT';
export default withMT({
    content: ["./index.html", "./src/**/*.{js,jsx,ts,tsx}"],
    theme: {
        extend: {},
    },
    plugins: [],
});
"""
        with open("tailwind.config.js", "w") as f:
            f.write(tailwind_config)
    
    if react:
        with open("tailwind.config.js", "w") as f:
            f.write("""
            module.exports = {
                public: "./index.html",
                content: ["./src/**/*.{js,jsx,ts,tsx,html}"],
                theme: {
                    extend: {},
                },
                plugins: [],
            };

""")
        with open("src/index.css", "w") as f:
            f.write("@tailwind base;\n@tailwind components;\n@tailwind utilities;")
        
        os.makedirs(".vscode", exist_ok=True)
        with open(".vscode/settings.json", "w") as f:
            f.write("""   {"editor.formatOnSave": true,
    "files.associations": { "*.css": "tailwindcss" },

    "tailwindCSS.includeLanguages": {
        "html": "html",
        "javascript": "javascript",
        "css": "css"
    },
    "editor.quickSuggestions": {
        "strings": true
    }
}
        """  
        )
        setup_prettier()
        with open("src/App.css", "w") as f:
            f.write("")
        
        
def create_mern(project_name, github_repo=None):
    # Create project folder
    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)

    # Initialize git repository
    if github_repo:
        os.system(f"ga init {github_repo}")
    else:
        os.system("ga init")
    
    # Create backend folder and setup Node project
    os.makedirs("backend", exist_ok=True)
    os.chdir("backend")
    create_node_project(".")
    os.chdir("..")

    # Create frontend folder and setup React project
    os.makedirs("frontend", exist_ok=True)
    os.chdir("frontend")
    create_react_project(".")
    os.chdir("..")

    print("MERN project setup complete")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("""
Usage: script.py <project_type> [project_name] [additional_options]

Functions:
  -fe            Create a frontend web project using Vite and React.
  -django        Create a Django project with optional app name.
  -react         Create a React project using Vite.
  -react-ts      Create a TypeScript React project using Vite.
  -node          Create a Node.js project with Express.
  -mern          Create a MERN stack project with both backend (Node.js) and frontend (React).

Additional Options:
  -start         Start the development server for the selected project type.
  -cc            Create a React component with optional directory and CSS flag.
  -mp            Deploy a React project to GitHub Pages with optional page name.
  -tw            Set up Tailwind CSS for a React project.
  -gethooks      Copy custom hooks to the 'src/hooks' directory.


""")
        sys.exit(1)

    project = sys.argv[1]
    flag = sys.argv[2] if len(sys.argv) > 2 else sys.argv[1]
    print(project)
    args = sys.argv
    print(args)
    if "-start" in args:
        start_project(project)
        sys.exit()
    elif flag == "-cc":
        create_react_component(nodir= "-nodir" in args,component_name= args[3] if len(args)> 3   else 'Component',create_css= "-css" in args, ts="-ts" in args, dir='components' )
    elif flag == "-cp":
        create_react_component(nodir= "-nodir" in args,component_name= args[3] if len(args)> 3   else 'Component',create_css= "-css" in args, ts="-ts" in args, dir='pages' )
    elif flag == "-prettier":
        setup_prettier()
    elif flag == "-mp":
        deploy_react_project(args[2] if len(args) > 2 else 'Page', ts="-ts" in args)
    elif flag == "-tw":
        setup_tailwind(react=(project=="react"), material_tailwind="-mt" in args)
    elif flag == "-gethooks":
        copy_hooks()
    elif project in ["1", "fe"]:
        create_fe_project(args[2] if len(args) > 2 else "mywebapp")
    elif project in ["2", "django"]:
        create_django_project(projectname=args[2] if len(args) > 2 else "mydjangoproject",appname= args[3] if len(args) > 3 else "mydjangoapp")
    elif project in ["3", "react"]:
        create_react_project(args[2] if len(args) > 2 else "my-react-app")
    elif project in ["4", "react-ts"]:
        create_react_project(args[2] if len(args) > 2 else "my-react-ts-app", ts=True)
    elif project in ["5", "node"]:
        create_node_project(args[2] if len(args) > 2 else "my-node-app")
    elif project in ["6", "mern"]:
        create_mern(project_name=args[2] if len(args)>2 else "my-mern_project",github_repo=args[2] if len(args)>2 else None)

    else:
        print("Invalid choice")
        sys.exit(1)
