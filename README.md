# Environment Setup

This demo project relies on a few tools to demonstrate a production-ready environment.

* [Homebrew](https://brew.sh/) to install direnv on osx.
* [virtualenv](https://docs.python.org/3/library/venv.html) to configure a virtual Python environment
* [direnv](https://direnv.net/docs/hook.html) for additional protection of env vars.

'''shell
# Install direnv via Homebrew
brew update && brew bundle install

# Setup [direnv](https://direnv.net/docs/hook.html)  if not installed, .e.g.
vim ~/.zshrc
eval "$(direnv hook zsh)"

# Reload your terminal and Trust the .envrc file
direnv allow

# Create and activate the python venv
pip install virtualenv
python3.12 -m venv env

# Enter the virtual environment using
source env/bin/activate

# To exit, you can use
deactivate

# Install python packages
pip install --upgrade pip && pip install -r requirements.txt
'''

# We will also need to populate the environment variables we need in an .envrc file.
'''
vim .envrc
export HOMEBREW_BUNDLE_NO_LOCK=1
export SECRET_KEY="YourLocalSecretKey"
export DEBUG=True
'''

# Next, run the migrations
'''
python manage.py migrate
'''
# Rabbitmq Broker Setup
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management


# Running a Celery Worker
celery -A trabu_backend worker -l INFO


# Architecture Decision Records (ADR)

Architecture Decision Records are a recommended best practice and help new team members to onboard quickly, 
understanding why key decisions were made and which problems were trying to be solved.

Project members should create an ADR for every architecturally significant decision that affects the software project 
or product, including the following (Richards and Ford 2020):
- Structure (for example, patterns such as microservices)
- Non-functional requirements (security, high availability, and fault tolerance)
- Dependencies (coupling of components)
- Interfaces (APIs and published contracts)
- Construction techniques (libraries, frameworks, tools, and processes)

The '/docs/architecture-decision-records' directory contains ADR files following the template in
[Documenting architecture decisions - Michael Nygard](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions).

For more information, please read the AWS prescriptive-guidance at:
https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html
