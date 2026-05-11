### Story 1 - Basic Room Booking:
 As a Employee, I want to search for and book an available conference room on a specific day and time. So that I can reserve a space for a meeting without manually coordinating with other teams

 ### Acceptance Criteria:
    - Given I am logged in,When i select a date, start time and end time, Then I see a list of available rooms for that slot
    - Given a room is already booked for a time slot, When I search for that slot, Then the room does not appear in the available results

### Story Points:
    5

### Priority:
    High
### Dependencies:
    None

### Technical Notes:
    -Room availability must be calculated in real time against the bookings database
    -Booking confirmation should trigger both email and in-app notifications
    -Time slots should be in 30-minute increments
    -System must prevent double-booking at the database transaction level

### Design Notes:
    -Calendar/time picker should be intuitive and mobile-friendly
    -Available rooms should be displayed as cards with key info (name, floor, capacity, equipment)
    -Confirmation screen should show a full summary before final submission