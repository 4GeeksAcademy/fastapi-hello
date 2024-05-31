<a href="https://www.breatheco.de"><img height="280" align="right" src="https://github.com/4GeeksAcademy/fastapi-hello/blob/main/.devcontainer/badge-fastapi.png?raw=true"></a>

# The Smalles possible FastAPI Template

Create an API's using FastAPI in just minutes, [📹 watch the video tutorial](https://youtu.be/ORxQ-K3BzQA).

- [Extensive documentation here](https://4geeks.com/docs/start/start-fastapi).
- Integrated with Pipenv for package managing.
- Fast deloyment to render.com or heroku with `$ pipenv run deploy`.
- Use of `.env` file.
- SQLAlchemy integration for database abstraction.

## 1) Installation

This template installs itself in a few seconds if you open it for free with Codespaces (recommended) or Gitpod.
Skip this installation steps and jump to step 2 if you decide to use any of those services.

> Important: The boiplerplate is made for python 3.10 but you can change the `python_version` on the Pipfile.

The following steps are automatically runned withing Codespaces or Gitpod, if you are doing a local installation you have to do them manually:

```sh
# Install packages
pipenv install;

# Create postgres database
psql -U root -c 'CREATE DATABASE example;'

# Initialize migrations
pipenv run init;

# Create your first migration
pipenv run migrate;

# Upgrade for the first time
pipenv run upgrade;
```

> Note: Codespaces users can connect to psql by typing: `psql -h localhost -U gitpod example`

## 2) How to Start coding

There is an example API working with an example database. All your application code should be written inside the `./src/` folder.

- src/endpoints/<file>.py: it's where your endpoints should be coded; add one file for each model, for example, `./src/endpoints/user.py.`
- src/models.py: your database tables and serialization logic.
- src/utils.py: some reusable classes and functions.
- src/admin.py: add your models to the admin and manage your data easily.
- src/database.py: Do not modify this file, database configuration.

For a more detailed explanation, look for [extensive documentation here](https://4geeks.com/docs/start/start-fastapi).

## Remember to migrate every time you update your models

You have to migrate and upgrade the migrations for every update you make to your models:

```bash
$ pipenv run migrate # (to make the migrations)
$ pipenv run upgrade  # (to update your database with the migrations)
```

## Check your API live

1. Once you run the `pipenv run start` command your API will start running live and you can open it by clicking in the "ports" tab and then clicking "open browser".

> ✋ If you are working on a coding cloud like [Codespaces](https://docs.github.com/en/codespaces/developing-in-codespaces/forwarding-ports-in-your-codespace#sharing-a-port) or [Gitpod](https://www.gitpod.io/docs/configure/workspaces/ports#configure-port-visibility) make sure that your forwared port is public.

## Publish/Deploy your website!

This boilerplate it's 100% read to deploy with Render.com and Herkou in a matter of minutes. Please read the official documentation about it:

- [Deploy to Render.com](https://4geeks.com/docs/start/deploy-to-render-com)
- [Deploy to Heroku](https://4geeks.com/docs/start/deploy-to-heroku)

### Contributors

This template was built as part of the 4Geeks Academy [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp) by [Alejandro Sanchez](https://twitter.com/alesanchezr) and many other contributors. Find out more about our [Full Stack Developer Course](https://4geeksacademy.com/us/coding-bootcamps/part-time-full-stack-developer), and [Data Science Bootcamp](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning).

You can find other templates and resources like this at the [school github page](https://github.com/4geeksacademy/).
