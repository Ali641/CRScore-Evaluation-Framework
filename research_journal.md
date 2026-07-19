# Research Journal

## Entry 1 – Project Initialization

Date: 2026-07-17

- Created GitHub repository.
- Configured Python development environment.
- Installed Git.
- Selected GitHub REST API as the primary data source instead of third-party libraries.
- Established repository selection criteria:
  - Language: Python
  - Public repositories
  - Not archived
  - Not forks
  - Stars ≥ 50
  - Minimum contributors ≥ 2 (to be verified after metadata collection)
- Decided to implement the project using a modular architecture to improve reproducibility and maintainability.

## Entry 2 – GitHub REST API Integration

Date: 2026-07-17

- Successfully authenticated with the GitHub REST API using a Personal Access Token.
- Implemented a reusable GitHub client module for API communication.
- Verified successful communication by retrieving authenticated user information.
- Prepared the repository collection module using the GitHub Search API with predefined repository selection criteria.

## Entry 3 – Repository Search Validation

Date: 2026-07-17

- Successfully queried the GitHub Search API using predefined repository selection criteria.
- Retrieved Python repositories sorted by popularity.
- Identified the GitHub Search API limitation of returning only the first 1,000 matching results.
- Decided to adopt a stratified sampling strategy using repository star ranges to obtain a more balanced and representative dataset.