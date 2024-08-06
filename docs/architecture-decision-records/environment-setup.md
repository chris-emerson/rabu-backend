
# Environment Setup

## Status

Accepted

## Context

The default Django project exposes sensitive database credentials in its settings.py file.
We want to set the repo up so that we don't accidentally check sensitive data into git.

## Decision

- Setup settings.py to load sensitive configuration data from the environment. 
- Install direnv via Homebrew to ensure that our environment file is only loaded and unloaded whilst we work on the project.
- Move env vars into an .envrc file
- Add .envrc to .gitignore

## Consequences

This configuration will make it harder for developers to accidentally check sensitive
credentials into git. Furthermore, we can leverage direnv in a container environment and 
write the .envrc file in the future using config generation scripts to pull the data from
Hashicorp Vault or AWS Secrets Manager.

The disadvantage is that it requires more setup and certain dependencies to be installed. 
This is partially mitigated by additional instructions in the readme and by using the 
popular virtualenv and direnv libraries.