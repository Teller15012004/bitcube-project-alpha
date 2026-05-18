# Conference Room Booking System

> A web-based system for managing and reserving shared meeting spaces within an organisation. Built during a sprint simulation as part of a structured software development training programme.

---

## Table of Contents

- [Project Overview](#project-overview)
- [System Context](#system-context)
- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [Sprint Artefacts](#sprint-artefacts)
- [Contribution Workflow](#contribution-workflow)
- [Future Technical Sections](#future-technical-sections)

---

## Project Overview

The **Conference Room Booking System** allows employees within an organisation to view available meeting rooms, make bookings, and manage reservations — all without needing to contact an administrator. It removes the friction of manually coordinating room availability and eliminates double-bookings.

**Who it is for:**
- **End users** – Employees who need to reserve a room for a meeting
- **Administrators** – Staff responsible for managing room availability and resolving conflicts
- **Developers** – Engineers onboarding to extend or maintain the system

This repository contains the source code, sprint documentation, and project artefacts produced during the development simulation.

---

## System Context

The system is structured around three major areas of responsibility:

| Component | Description |
|-----------|-------------|
| **Booking Engine** | Core logic for creating, updating, and cancelling reservations. Enforces availability rules and conflict detection. |
| **Room Management** | Handles the catalogue of rooms: capacity, location, equipment, and availability windows. |
| **User Interface** | The front-facing layer through which users interact with the system — browsing rooms, submitting bookings, and viewing their reservation history. |

These components communicate with a shared data layer. The system does not currently integrate with external calendar tools, though this is noted as a future enhancement.

---

## Getting Started

### Prerequisites

Before running this project locally, ensure you have the following installed:

- **Node.js** v18 or higher — [Download](https://nodejs.org/)
- **npm** v9 or higher (bundled with Node.js)
- **Git** — [Download](https://git-scm.com/)
- A code editor such as [VS Code](https://code.visualstudio.com/)

> **Note:** Database setup instructions will be added here once the persistence layer is finalised.

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Teller15012004/bitcube-project-alpha.git

# 2. Navigate into the project directory
cd conference-room-booking

# 3. Install dependencies
npm install

# 4. Start the development server
npm run dev
```

The application will be available at `http://localhost:3000` by default.

### Running Tests

```bash
npm test
```

---

## Sprint Artefacts

The `docs/` directory contains markdown artefacts produced during the sprint simulation. These are living documents and should be consulted when onboarding or reviewing the project's development history.

| Artefact | Location | Purpose |
|----------|----------|---------|
| Sprint Planning | `docs/sprint-planning/` | Goals, user stories, and task breakdown for each sprint |
| Retrospectives | `docs/retrospectives/` | Team reflections on process and delivery |
| System Diagrams | `docs/diagrams/` | High-level architecture and data flow visuals |
| Definition of Done | `docs/definition-of-done.md` | Acceptance criteria used during the sprint |

> New developers should read the most recent retrospective and sprint planning document before picking up any tasks.

---

## Contribution Workflow

This project uses **Pull Requests (PRs)** as the primary mechanism for contributing changes. Direct commits to `main` are not permitted.

### Step-by-Step

Create a branch from main
git checkout -b feature/your-feature-name
Make your changes with clear, atomic commits
Push your branch to the remote
git push origin feature/your-feature-name
Open a Pull Request on GitHub

Use the PR template provided
Link any relevant issues or sprint artefacts
Tag at least one teammate for review


Address review feedback
Merge only after approval

### Branch Naming Convention

| Type | Format | Example |
|------|--------|---------|
| Feature | `feature/short-description` | `feature/room-filter-ui` |
| Bug fix | `fix/short-description` | `fix/double-booking-error` |
| Documentation | `docs/short-description` | `docs/update-readme` |

### Pull Request Expectations

A well-formed PR should:
- Explain **why** the change is being made (not just what)
- Describe what reviewers should focus on
- Reference relevant sprint documentation or issues where applicable
- Be small enough to review in a single sitting

---

## Future Technical Sections

The following sections are placeholders for content to be added as the project matures:

- **[ ] Environment Variables** – List of required `.env` keys and their purpose
- **[ ] Database Setup** – Schema, migrations, and seed data instructions
- **[ ] API Reference** – Endpoint documentation
- **[ ] Deployment Guide** – CI/CD pipeline and production deployment steps
- **[ ] Authentication** – Login flow and role-based access control
- **[ ] Troubleshooting** – Common errors and their resolutions

---

*This README was last updated as part of Assignment 3.1 – Documentation & Pull Requests as Professional Communication.*

