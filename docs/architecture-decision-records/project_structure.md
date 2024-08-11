# Django Project Structure

## Status

Accepted

## Context

The team needs to decide on a module structure for the backend. 
We'll start with the requirements specification, generate some core use cases
and determine what any potential areas of change are by using volatility-decomposition.

Volatility-based decomposition identifies areas of potential change and encapsulates 
those into services or system building blocks. 

The following volatilities have been identified from the requirements.
- The requirements state that the backend should generate travel itineraries using GPT. 
  However, we might wish to use a different LLM in the future so we should ensure that 
  we encapsulate this change to prevent un-necessary code changes in the future.
- The team currently uses Celery as their distributed task queue. 
  This could potentially change in the future, although celery does offer a wide range of supported brokers.
- The backend address and authentication details celery uses to contact a broker could change. 
- The team might wish to split some functionality off in the future into dedicated microservices. 
  We should consider encapsulating features into modules that can make migrating easier.
- We should consider setting up a separate database schema for each app/feature so that apps and features 
  can be migrated in the future if needed.
- The technology used to communicate with the client could potentially change in the future. 
  Right now we are using REST, but what if we wanted to use websockets, gRPC or Server Side Events?

## Decision

The itinerary generation logic could get quite large over time and is potentially quite volatile
due to the complexity of LLM travel planning. Whilst we might decide to start off with a monolithic 
architecture for the MVP, over time it is likely to need its own service at some point.

- We should encapsulate the Planner as a Django application 
- In a production app we would also write a DatabaseRouter and have the Planner models use a separate schema.
  However, this is a bit beyond the scope of this exercise.
- We should factor some of the above volatilities into our interfaces and use SOLID principles to make the system 
easier to maintain, without straying too far away from the typical Django project structure.

## Consequences

Developers will need to be careful where they place their files and data to ensure that the 
module structure is preserved. Migrations will need to be run separately against the Planner db.
An increase in configuration complexity will be traded for migration flexibility in the future.