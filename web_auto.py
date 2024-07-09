#!/usr/bin/env python3
import shutil
import sys
import os
import sys
import json
import requests
from requests.auth import HTTPBasicAuth

def create_react_project(args):
    
    if "-cc" in args:
        create_react_component(args)
    elif "-mp" in args:
        deploy_react_project(args)
    elif "-gethooks" in args:
        copy_hooks()
    elif "-tw" in args:
        set_tailwind(args)
    else:
        projectname = args[1] if len(args) > 1 else "my-react-app"
        os.system(f"npm create vite@latest {projectname} -- --template react")
        os.chdir(projectname)
        os.system("npm install")
        os.system("code .")

def create_react_component(args):
    component_dir = args[3] if len(args) > 3 else 'components'
    component_name = args[4] if len(args) > 4 else 'Component'
    create_css = "-css" in args
    
    if not os.path.exists("src"):
        print("Error: src folder not found")
        sys.exit(1)
    
    os.chdir("src")
    if component_dir != '.':
        os.makedirs(component_dir, exist_ok=True)
        os.chdir(component_dir)
    
    if create_css:
        os.makedirs(component_name, exist_ok=True)
        os.chdir(component_name)
        with open(f"{component_name}.jsx", "w") as f:
            f.write(f"import React from 'react';\nimport './{component_name}.css'\nconst {component_name} = () => {{\nreturn (\n<div>\n<h1>{component_name}</h1>\n</div>\n)\n}}\n\nexport default {component_name};")
        open(f"{component_name}.css", 'a').close()
    else:
        with open(f"{component_name}.jsx", "w") as f:
            f.write(f"import React from 'react';\nconst {component_name} = () => {{\nreturn (\n<div>\n<h1>{component_name}</h1>\n</div>\n)\n}}\n\nexport default {component_name};")
    sys.exit()
def set_tailwind(args):
    os.system("npm install tailwindcss@latest postcss@latest autoprefixer@latest")
    os.system("npx tailwindcss init -p")
    tailwind_config = """
    module.exports = {
    content: [
        './public/index.html',
        './src/**/*.{js,jsx,ts,tsx}',
    ],
    theme: {
        extend: {},
    },
    plugins: [],
    }
    """
    with open("tailwind.config.js", "w") as f:
        f.write(tailwind_config)
    with open("src/index.css", "w") as f:
        f.write("@tailwind base;\n@tailwind components;\n@tailwind utilities;")
    os.mkdir(".vscode")
    with open(".vscode/settings.json", "w") as f:
        f.write("""{"editor.formatOnSave": true,
                "files.associations": {"*.css": "tailwindcss"},
                }""")
    with open("src/App.css", "w") as f:
        f.write("")
    with open("src/App.jsx", "w") as f:
        f.write("""
    import './App.css';
    import './index.css';
    import React from 'react';

    function App() {
    return (
        <>
        </>
    );
    }

    export default App;
    """)
def deploy_react_project(args):
    page_name = args[4] if len(args) > 4 else 'Page'
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
        os.system("git init")
    else:
        print("Repository already exists")
    
    os.system(f"git remote add origin https://github.com/{username}/{repo_name}.git")
    os.system("npm install gh-pages --save-dev")
    
    if "-pc" in args:
        os.system("git add .")
        os.system("git commit -m 'Deploying to GitHub Pages'")
        os.system("git push -u origin main")

    os.system("npm run build")
    update_vite_config()
    update_package_json(homepage)
    os.system("npm run deploy")
    print(f"Deployment successful. The page is live at {homepage}")
    sys.exit()

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
def create_react_ts_project(args):

    
    if "-cc" in args:
        create_react_ts_component(args)
    elif "-mp" in args:
        deploy_react_ts_project(args)
    elif "-gethooks" in args:
        copy_hooks()
    else:
        projectname = args[1] if len(args) > 1 else "my-react-ts-app"
        os.system(f"npm create vite@latest {projectname} -- --template react-ts")
        os.chdir(projectname)
        os.system("npm install")
        os.system("code .")
def copy_hooks():
    hooks_src_dir = "/usr/local/bin/hooks"  # Update this path to your custom hooks directory

    # Create hooks directory if not exists
    os.makedirs("src/hooks", exist_ok=True)

    # Copy custom hooks
    for hook_file in os.listdir(hooks_src_dir):
        full_file_name = os.path.join(hooks_src_dir, hook_file)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, "src/hooks")
def create_react_ts_component(args):
    component_dir = args[3] if len(args) > 3 else 'components'
    component_name = args[4] if len(args) > 4 else 'Component'
    create_css = "-css" in args
    
    if not os.path.exists("src"):
        print("Error: src folder not found")
        sys.exit(1)
    
    os.chdir("src")
    if component_dir != '.':
        os.makedirs(component_dir, exist_ok=True)
        os.chdir(component_dir)
    
    if create_css:
        os.makedirs(component_name, exist_ok=True)
        os.chdir(component_name)
        with open(f"{component_name}.tsx", "w") as f:
            f.write(f"import React from 'react';\nimport './{component_name}.css'\nconst {component_name} = () => {{\nreturn (\n<div>\n<h1>{component_name}</h1>\n</div>\n)\n}}\n\nexport default {component_name};")
        open(f"{component_name}.css", 'a').close()
    else:
        with open(f"{component_name}.tsx", "w") as f:
            f.write(f"import React from 'react';\nconst {component_name} = () => {{\nreturn (\n<div>\n<h1>{component_name}</h1>\n</div>\n)\n}}\n\nexport default {component_name};")
    sys.exit()

def deploy_react_ts_project(args):
    page_name = args[4] if len(args) > 4 else 'Page'
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
        os.system("git init")
    else:
        print("Repository already exists")
    
    os.system(f"git remote add origin https://github.com/{username}/{repo_name}.git")
    os.system("npm install gh-pages --save-dev")
    
    if "-pc" in args:
        os.system("git add .")
        os.system("git commit -m 'Deploying to GitHub Pages'")
        os.system("git push -u origin main")

    os.system("npm run build")
    update_vite_config()
    update_package_json(homepage)
    os.system("npm run deploy")
    print(f"Deployment successful. The page is live at {homepage}")
    sys.exit()

def create_node_project(args):
    projectname = args[1] if len(args) > 1 else "my-node-app"
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

def create_django_project(args):
    projectname = args[1] if len(args) > 1 else "mydjangoproject"
    appname = args[2] if len(args) > 2 else "mydjangoapp"
    
    # Step 1: Create Django project
    ret = os.system(f"django-admin startproject {projectname}")
    if ret != 0:
        print("Error in creating project")
        c = input("Do you want to try again? (y/n): ")
        if c.lower() != 'y':
            sys.exit()
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
    
    # Step 6: Update settings.py for templates, static, and media directories
    with open(f"{projectname}/settings.py", "r") as f:
        lines = f.readlines()
    
    # Find the position to add our configurations
    import_index = -1
    for i, line in enumerate(lines):
        if 'import os' in line:
            import_index = i + 1
            break
    
    # Define paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    templates_dir = os.path.join(BASE_DIR, 'templates')
    static_dir = os.path.join(BASE_DIR, 'static')
    media_dir = os.path.join(BASE_DIR, 'media')
    
    # Modify settings.py
    updated_lines = lines[:import_index]
    updated_lines.append('\n')
    updated_lines.append(f'TEMPLATES[0]["DIRS"] = [os.path.join(BASE_DIR, "templates")]\n')
    updated_lines.append('\n')
    updated_lines.append(f'STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]\n')
    updated_lines.append('\n')
    updated_lines.append(f'MEDIA_ROOT = os.path.join(BASE_DIR, "media")\n')
    updated_lines.append('\n')
    updated_lines.append('MEDIA_URL = "/media/"\n')
    updated_lines.append('\n')
    
    # Write back to settings.py
    with open(f"{projectname}/settings.py", "w") as f:
        f.writelines(updated_lines)
    
    # Step 7: Make initial migrations
    os.system("python3 manage.py makemigrations")
    os.system("python3 manage.py migrate")
    
    # Step 8: Open VS Code
    os.system("code .")
def create_fe_project(args):
    projectname = args[1] if len(args) > 1 else "mywebapp"
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
        print("Invalid project type for starting environment")
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: script.py <project_type> [project_name] [additional_options]")
        sys.exit(1)

    project = sys.argv[1]
    args = sys.argv[1:]
    if "-start" in sys.argv:
        start_project(project)
        sys.exit()
    if project in ["1", "fe"]:
        create_fe_project(args)
    elif project in ["2", "django"]:
        create_django_project(args)
    elif project in ["3", "react"]:
        create_react_project(args)
    elif project in ["4", "react-ts"]:
        create_react_ts_project(args)
    elif project in ["5", "node"]:
        create_node_project(args)
    else:
        print("Invalid choice")
        sys.exit(1)
