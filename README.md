# Rabu Demo Backend

This repository contains logic to provide a backend for a Generative AI search application. The application allows the user to discover new Trip ideas by clicking around a map. It uses ChatGPT to plan a three day trip of local attractions and then renders the Itinerary on a map.

![UseCases](docs/app_preview2.png?raw=true)

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
This demo project is not secure. CORS has been disabled for development purposes since this is not intended for production usage. The only precaution taken is to use direnv to reduce the chance of accidental API key leakage.

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

## Admin
The django admin page can be accessed at: 
```http://127.0.0.1:8000/admin/```

The admin page has also been configured with `django-celery-results` to incldue Celery results so that 
we can keep track of the Async Worker tasks.
![CeleryTasks](docs/celery_task_results.png?raw=true)

# API Responses & Format

The REST api returns responses in JSON:API format. In a production app you would leverage Hypermedias as the Engine of Application of State (HATEOAS) but the service requires more configuration to include the hypermedia links. Hypermedia is beneficial as it helps to navigate through your platform and encourages loose coupling ofclients to the backend. 

The application is built around restful resources. We POST a request to the /itinerary-generation/ endpoint to generate a new Itinerary Generation resource. Whilst not yet implemented, this endpoint is considered a resource in its own right and could keep track of request metadata, search params etc as well as the current status of the async processing. 

After processing, the backend then creates a new Itinerary resource which can be accessed at /v1/itineraries/:id as required. Access to subresources is possible but not encourages due to DDD principles. 

Endpoints:
* POST /itinerary-generation
* GET /v1/itineraries/:id
  
```json
GET /v1/itineraries/801/
HTTP 200 OK
Allow: GET
Content-Type: application/vnd.api+json
Vary: Accept

{
    "data": {
        "type": "itinerary",
        "id": "801",
        "attributes": {
            "label": "Trip to Sainte-Adresse, Seine-Maritime, France",
            "created_at": "2024-08-11T01:40:01.335505Z",
            "updated_at": "2024-08-11T01:40:04.192831Z",
            "itinerary_item_groups": [
                {
                    "id": 2352,
                    "label": "Day 1",
                    "created_at": "2024-08-11T01:40:01.337680Z",
                    "updated_at": "2024-08-11T01:40:01.337645Z",
                    "itinerary": {
                        "type": "itineraries",
                        "id": "801"
                    },
                    "itinerary_items": [
                        {
                            "id": 4724,
                            "created_at": "2024-08-11T01:40:01.804747Z",
                            "updated_at": "2024-08-11T01:40:01.804716Z",
                            "activity": {
                                "type": [
                                    "activity"
                                ],
                                "id": "4726"
                            },
                            "group": {
                                "type": [
                                    "itinerary_item_group"
                                ],
                                "id": "2352"
                            },
                            "activity_data": {
                                "id": 4726,
                                "description": "Visit the Cliffs of Etretat",
                                "created_at": "2024-08-11T01:40:01.802622Z",
                                "updated_at": "2024-08-11T01:40:01.802564Z",
                                "itinerary_item": [
                                    {
                                        "type": "itinerary_items",
                                        "id": "4724"
                                    }
                                ],
                                "image": "http://static1.squarespace.com/static/5fa57aacf5b0a90a76b0d7cc/t/615b193d7eb5903949fd11b4/1633360189924/HYW_20190917_203335-squarespace.jpg?format=1500w",
                                "full_description": "Experience the breathtaking views of the iconic Cliffs of Etretat, famous for their stunning white chalk cliffs, natural arches, and pebble beaches. Walk along the cliff paths, admire the dramatic scenery, and capture unforgettable moments with your family."
                            },
                            "latitude": 49.708131,
                            "longitude": 0.202447
                        },
                        {
                            "id": 4725,
                            "created_at": "2024-08-11T01:40:02.358412Z",
                            "updated_at": "2024-08-11T01:40:02.358401Z",
                            "activity": {
                                "type": [
                                    "activity"
                                ],
                                "id": "4727"
                            },
                            "group": {
                                "type": [
                                    "itinerary_item_group"
                                ],
                                "id": "2352"
                            },
                            "activity_data": {
                                "id": 4727,
                                "description": "Explore Le Havre City Center",
                                "created_at": "2024-08-11T01:40:02.356885Z",
                                "updated_at": "2024-08-11T01:40:02.356856Z",
                                "itinerary_item": [
                                    {
                                        "type": "itinerary_items",
                                        "id": "4725"
                                    }
                                ],
                                "image": "https://acis.com/wp-content/uploads/2013/12/120313_blog_featured.png",
                                "full_description": "Immerse yourself in the vibrant atmosphere of Le Havre City Center, a UNESCO World Heritage site known for its modernist architecture and cultural richness. Discover charming cafes, historic buildings, and bustling markets as you wander through the heart of the city."
                            },
                            "latitude": 49.487957,
                            "longitude": 0.112878
                        }
                    ]
                }]
            }
        }
}
```