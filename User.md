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

### Story #4: Booking Cancellation
    As a Employee, I want to cancel a room booking I have made. So that the room becomes available for other colleagues when I no longer need it

### Acceptance Criteria:
    -Given I have an upcoming booking, When I navigate to "My Bookings" and select a booking, Then I see an option to cancel it
    -Given I initiate a cancellation, When I confirm the action, Then the booking is removed, the room is freed, and I receive a cancellation confirmation
    -Given a booking is within a restricted cancellation window (e.g., less than 15 minutes before start time), When I attempt to cancel, Then I am warned and must contact the admin or receptionist to proceed

### Story Points:
    3

### Priority:
    High

### Dependencies:
    Story #1: Basic Room Booking

### Technical Notes:
    -Cancelled bookings should be soft-deleted (status set to CANCELLED) to preserve audit history
    -Cancellation should trigger a notification to any attendees listed on the booking

### Design Notes:
    -Cancellation must require a confirmation step (Confirm/Cancel) to prevent accidental deletions
    -Clearly display the cancellation deadline on the booking detail view
    -"My Bookings" view should have clear visual distinction between upcoming, past, and cancelled bookings

### Story #5: Room Equipment Requirements
    As a Employee, I want to filter rooms by available equipment (e.g., projector, whiteboard, video conferencing). So that I can book a room that has the tools my meeting requires

### Acceptance Criteria:
    -Given I am searching for rooms, When I select one or more equipment filters, Then only rooms with all selected equipment items are shown in the results
    -Given a room is listed, When I view its details, Then I see a complete list of all available equipment in that room
    -Given I book a room, When the booking confirmation is shown, Then the confirmed equipment list for that room is included in the summary

### Story Points:
    3

### Priority:
    Medium

### Dependencies:
    -Story #1: Basic Room Booking
    -Story #3: Room Capacity Filtering

### Technical Notes:
    -Equipment is stored as a many-to-many relationship between rooms and equipment_types tables
    -Equipment catalogue (types/names) should be managed by the admin

### Design Notes:
    -Equipment filters should display as checkboxes with recognisable icons (projector icon, camera icon, etc.)
    -Combine equipment and capacity filters into a single collapsible "Advanced Filters" panel
    -Equipment shown on room cards should use icon badges to keep the UI compact

### Story #6: Admin Dashboard Viewing
    As an Admin, I want to view a real-time dashboard showing all current and upcoming bookings across all rooms. So that I can monitor room utilisation and respond quickly to any issues or conflicts.

### Acceptance Criteria:

    -Given I am logged in as an Admin, When I navigate to the dashboard, Then I see a room-by-room timeline view of all bookings for the current day
    -Given the dashboard is open, When a new booking is made or cancelled by any user, Then the dashboard updates within 30 seconds without requiring a page refresh
    -Given I click on a booking on the dashboard, When the booking detail panel opens, Then I see the organiser's name, attendee count, meeting title, and equipment in use

### Story Points:
    8
### Priority:
    High

### Dependencies:
    _Story #1: Basic Room Booking
    -Story #10: Usage Reports Generation

### Technical Notes:
    -Initial load must complete within 3 seconds for up to 50 rooms
    -Access to this view must be restricted to users with the ADMIN role

### Design Notes:
-Gantt-style horizontal timeline per room is the recommended layout for the day view
-Include a date picker to navigate to past or future days
-Colour-code bookings by status: confirmed (green), pending (yellow), maintenance (grey)

### Story #7: Room Maintenance Scheduling
    As a Facilities Manager, I want to block out rooms for scheduled maintenance or deep cleaning. So that employees cannot book a room that is unavailable due to facilities work
h
### Acceptance Criteria:
    -Given I am logged in as a Facilities Manager, When I select a room and a date/time range and mark it as "Under Maintenance," Then that room is unavailable for booking during that period
    -Given a maintenance block is active, When an employee searches for rooms, Then the blocked room does not appear in search results for the affected period

### Story Points:
    5

### Priority:
    Medium

### Dependencies:
    -Story #1: Basic Room Booking
    -Story #4: Booking Cancellation

### Technical Notes:
    -Maintenance blocks should be stored as a separate maintenance_schedules table, not as bookings
    -Conflict detection must query both bookings and maintenance_schedules tables
    -Role-based access: only FACILITIES_MANAGER and ADMIN roles can create maintenance blocks

### Design Notes:
    -Maintenance scheduling interface should be accessible from the room management section
    -When conflicts exist, display affected bookings in a clear list with organiser contact info
    
### Story #8: Visitor Booking Assistance
    As a Receptionist, I want to create and manage room bookings on behalf of visitors or employees who request assistance at the front desk. So that guests and staff without system access can still have meetings accommodated.

### Acceptance Criteria:
    -Given I am logged in as a Receptionist, When I initiate a booking on behalf of a user, Then I can search and book any available room and assign it to the requesting employee's or visitor's name
    -Given I am creating a visitor booking, When I enter the visitor's name and host employee, Then the booking record reflects both the visitor as the attendee and the host as the contact person
    -Given a booking has been created on behalf of a visitor, When I view the booking, Then it is clearly labelled as a "Receptionist-Assisted" booking with my name as the creator

### Story Points:
    5

### Priority:
    Medium

### Dependencies:
    -Story #1: Basic Room Booking
    -Story #3: Room Capacity Filtering
    -Story #5: Room Equipment Requirements

### Technical Notes:
    -Booking record schema must include created_by, booked_for_name, and booking_type (SELF/ASSISTED) fields
    -Receptionist role must have permission to book on behalf of others without impersonating them
    -Visitor entries do not require a system account; name and contact number are sufficient

### Design Notes:
    -Auto-complete for internal employees; free-text entry for external visitors
    -Receptionist's "My Bookings" view should list all bookings they have created, including assisted ones


