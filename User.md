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

### Story 2 - Story #2: Recurring Meeting Setup
    As a Employee, I want to schedule a recurring meeting (daily, weekly, or monthly) in a single booking action. So that I do not have to manually re-book the same room each time for standing meetings
    
### Acceptance Criteria:

    -Given I am creating a booking, When I enable the "Recurring" option and choose a frequency and end date, Then the system creates individual booking instances for each occurrence.
    -Given I have a recurring booking, When I cancel a single occurrence, Then only that occurrence is removed and the rest of the series remains intact

### Story Points:
    8

### Priority:
    High

### Dependencies:
    Story #1: Basic Room Booking

### Technical Notes:
    -Recurring logic should support: daily, weekly, monthly
    -Each occurrence stored as an individual record linked by a series_id for series-level management
    -Bulk insert of recurring instances must be handled as an atomic database transaction

### Design Notes:
    -Recurrence options should expand inline (progressive disclosure) rather than navigating to a new page
    -Clearly distinguish between "cancel this occurrence" and "cancel all future occurrences" in the UI

### Story #3: Room Capacity Filtering
    As a Employee, I want to filter available rooms by minimum seating capacity. So that I can quickly find a room that comfortably fits all meeting attendees.

### Acceptance Criteria:
    -Given I am searching for rooms, When I enter a required number of attendees, Then only rooms with a capacity greater than or equal to that number are shown
    -Given I apply a capacity filter, When no rooms meet the criteria for the selected time slot, Then I see a clear message indicating no rooms are available and am prompted to adjust my search
    
### Story Points:
    2

### Priority:
    High

### Dependencies:
    Story #1: Basic Room Booking

### Technical Notes:
    -Room capacity data must be maintained in the rooms master table
    -Capacity field should accept numeric input with validation (positive integers only)

### Design Notes:
Attendee count input should be prominent in the search form, alongside date and time
Consider a slider or stepper component for ease of use on mobile
Rooms slightly below capacity (e.g., 1–2 seats short) could be shown in a secondary "near match" section

