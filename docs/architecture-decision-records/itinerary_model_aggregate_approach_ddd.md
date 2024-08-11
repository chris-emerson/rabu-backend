
# Itinerary Models & Domain Driven Design

## Status

Accepted

## Context

A travel Itinerary is a potentially complex abstraction containing multiple items, sorted and grouped in various ways.
Changing a single item in the Itinerary could have a drastic effect on the rest of the Itinerary. 
In the book Domain Driven Design - Tackling Complexity in the Heart of Software (Evans, 2004), Eric Evans 
suggests making a single object the root aggregate in this kind of scenario.

To make this abstraction easier to manage and modify in the future, we will treat the Itinerary model 
as a root aggregate. In DDD terms, the root aggregate is essentially responsible for controlling access to the model 
and managing the state of the other related entities in the context. 

See Domain Driven Design by Eric Evans pg125 for further details.

## Decision

- We will add methods to the root aggregate (Itinerary) to manage the Itinerary
- Child models and tables ItineraryItem and ItineraryItemGroup should not be queried or modified directly.

## Consequences

The Itinerary abstraction will be easier to manage over time because the complexity of managing state 
and lifecycle events is encapsulated. However, developers unfamiliar with DDD might not understand why this
is an important discipline to follow.