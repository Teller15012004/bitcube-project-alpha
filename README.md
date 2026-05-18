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



