# Rabu Demo Backend

This repository contains logic to provide a backend for a Generative AI search application. The application allows the user to discover new Trip ideas by clicking around a map. It uses ChatGPT to plan a three day trip of local attractions and then renders the Itinerary on a map.

![UseCases](docs/app_preview.png?raw=true)

This repository contains the backend that powers the app by performing LLM a search query, geocoding tasks and image retrieval for the sample application.

![UseCases](docs/uml/main_sequence.png?raw=true)

## Environment Setup

This demo project relies on a few tools to demonstrate a production-ready environment.

* [Homebrew](https://brew.sh/) to install direnv on osx.
* [virtualenv](https://docs.python.org/3/library/venv.html) to configure a virtual Python environment
* [direnv](https://direnv.net/docs/hook.html) for additional protection of env vars.

```shell
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

# ps. To exit the venv, you can use
deactivate

# Install python packages
pip install --upgrade pip && pip install -r requirements.txt
```
### Environment Variables

```shell
# You will also need to populate the environment variables we need in an .envrc file. For demo purposes these can be provided by the author, provided they are not shared and destroyed after use.

vim .envrc
export HOMEBREW_BUNDLE_NO_LOCK=1
export SECRET_KEY="YourLocalSecretKey"
export DEBUG=True

# Google Custom Search for Images
export GOOGLE_IMAGE_CX="<YourCustomEndpointCX>"
export GOOGLE_IMAGE_API_KEY="<YourApiKey>"

# Mapbox for Geolocation APIs
export MAPBOX_API_TOKEN="<YourApiKey>"

# Chat GPT
export OPENAI_API_KEY="<YourApiKey>"
```

## Database Setup
This project is configured to use sqllite.

```shell
# Run the migrations
python manage.py migrate
```

## Celery & Rabbitmq
This demo app uses Celery and RabbitMQ. You can get up and running quickly with the following commands:

```shell
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management

# Running a Celery Worker
celery -A trabu_backend worker -l INFO
```
# Security & CORS
This demo project is not secure. CORS has been disabled for development purposes since this is not intended for production usage. The only precaution taken is to use direnv to reduce the chance of accidental credential leakage.

# Documentation

### Diagrams & Use Cases (PlantUML)
Whilst developingt he domain model for this project, it was helpful to capture some use cases for the basic requirements together with a bsaic domain model for the database.

![UseCases](docs/uml/use_cases.png?raw=true)

The basic database model is shown below. The domain was modelled to allow activities to be associated with an inventory item and grouped together into different sub-groups belonging to a single Inventory. In a microservices environment, an Itinerary-service might act as the root aggregate for managing access/coordinating the lifecycle and changes to an Itinerary. Activities would be managed separately.

![UseCases](docs/uml/data_model.png?raw=true)

### Architecture Decision Records (ADR)

Architecture Decision Records are a recommended best practice and help new team members to onboard quickly, understanding why key decisions were made and which problems were trying to be solved. This project contains some examples of ADR's to document some of the core dcecision making that took place.

**Architecture Decisions:**
  * [Environment Setup](./docs/architecture-decision-records/environment-setup.md)

  * [Project Structure](./docs/architecture-decision-records/project_structure.md)
  * [DDD approach for Itinerary model](./docs/architecture-decision-records//itinerary_model_aggregate_approach_ddd.md)

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
