# Sprint 1 Planning Session
    Date:13 May 2026
    Sprint Goal: To complete this weeks tasks on time.
## Attendees
    - Product Owner: Khauhelo Koto
    - Scrum Master: Kutlwano Moduka
    - Development Team: khauhelo Koto, Itumeleng Shaka, Mohammad Amla
## Velocity Target
    18 story points for Sprint 1
## Selected User Stories
    | Story # | Title | Story Points |
    |---------|-------|---------------|
    | Story #1 | Basic Room Booking | 5 |
    | Story #3 | Room Capacity Filtering | 2 |
    | Story #4 | Booking Cancellation | 3 |
## Dependencies
    - Story #3 depends on Story #1
    - Story #4 depends on Story #1
## Risks
    | Risk | Probability | Impact | Mitigation |
|------|-------------|---------|------------|
| Booking conflict logic may fail under overlapping requests | Medium | High | Add backend validation and database transaction locking |
| Delays in frontend and backend integration | Medium | Medium | Use API contracts early and test incrementally |
| Incorrect room availability calculations | Medium | High | Implement automated tests for booking logic |
| Scope creep during Sprint 1 | Low | Medium | Focus only on selected sprint backlog stories |
## Standup Cadence
    Time: 09:00
    Format: Coding for the Basic room booking was completed / Starting with coding the Room Capacity Filtering feature / Blockers:1