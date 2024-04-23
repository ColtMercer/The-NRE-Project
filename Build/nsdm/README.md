# Network State Data Machine (NSDM)
The Network State Data Machine (NSDM) is a event driven microservice that provides the follow services:
- **Nautobot Data** - Collects data from the network to be stored in Nautobot
- **Tools Integration** - When required can ensure all tools are integrated with Nautobot inventory
- **Configuration Data** - Collects configuration data from the network to be stored in a repository for Nautobot for Golden Config and indexed in Elastic for search capabilities
- **Data Change Response** - In general any data change in Nautobot that requires action to be taken will be handled by NSDM

## NSDM Microservices
The NSDM is broken down into the following microservices:
- **Collection Engine** - Collects data from the network and indexes the data in Elastic
- **Event Engine** - Listens for events on a Kafka topic and triggers actions based on the event
- **Scheduling Engine** - Schedules tasks to be run at a specific times
- **State Engine** - When triggered by changes to the network state, updates the state data in Nautobot
- **Nornir** - A microservice that runs Nornir scripts to collect data from the network

## NSDM Architecture
The NSDM is built on a microservices architecture that is event driven. The NSDM is built on the following technologies:
- **Microservices** - Each microservice is a containerized application written in Go for performance reasons. The exception is Nornir which is written in Python
- **Kafka** - The event bus that all microservices listen to for events