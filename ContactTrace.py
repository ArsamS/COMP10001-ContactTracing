def visit_length(visit):
    '''
    Returns the length of a person's visit in the format: (hours, minutes).
    '''
    
    if visit[5] >= visit[3]:
        # Calculate the total minutes and convert to hours and minutes
        difference = (visit[5] * 60 + visit[6]) - (visit[3] * 60 + visit[4])
        hours = difference // 60
        minutes = difference % 60
        
        # Return the calculations we made prior for valid visits
        if hours + minutes > 0:
            length = (hours, minutes)
            return length
        
        else: 
            return None

def contact_event(visit_a, visit_b):
    '''
    Calculates whether two valid visits overlap.
    '''
    
    # First, initialise variables
    overlap = False
    period_a = []
    period_b = []
    
    # Secondly, we will store visit periods as (start, end)
    # in total minutes to make calculations easier
    period_a.append(visit_a[3] * 60 + visit_a[4])
    period_a.append(visit_a[5] * 60 + visit_a[6])

    # Do the same for visit B
    period_b.append(visit_b[3] * 60 + visit_b[4])
    period_b.append(visit_b[5] * 60 + visit_b[6])
    
    # Test whether both visits are valid
    if period_a[0] < period_a[1] and period_b[0] < period_b[1]:
            # Make sure different people are visiting, locations are the same,
            # days of visit are the same, and that a visit is not empty
            if (visit_a[0] != visit_b[0] and visit_a[1] == visit_b[1] and
                    visit_a[2] == visit_b[2] and
                    period_a[0] + period_a[1] > 0 and
                    period_b[0] + period_b[1] > 0):

                # CASE 1: Starting later (ends within timeframe)
                if (period_b[0] > period_a[0] and 
                        period_b[0] < period_a[1]):
                    overlap = True

                # CASE 2: Starting earlier (ends within timeframe)
                elif (period_b[0] < period_a[0] and 
                        period_b[1] > period_a[0]):
                    overlap = True

                # CASE 3: Start at the same time
                elif (period_b[0] == period_a[0] and 
                        period_b[1] != period_a[1]):
                    overlap = True
            
            return overlap
    
    else:
        return None

def potential_contacts(person_a, person_b):
    '''
    Returns contact hours and locations between two people and
    their total interaction time based on valid input.
    '''
    
    # Firstly, initialise variables
    overlap_set = set()
    total = 0
    
    for a in range(len(person_a)):
        
        # Secondly, compare every visit in A's list to every visit in B's
        # where the location is the same
        for b in range(len(person_b)):
            if person_a[a][1] == person_b[b][1]:
                
                # Initialise contact period tuples
                overlap = False
                period_a = []
                period_b = []
                
                # Calculate visit periods so they can be compared
                period_a.append(person_a[a][3] * 60 + person_a[a][4])
                period_a.append(person_a[a][5] * 60 + person_a[a][6])

                period_b.append(person_b[b][3] * 60 + person_b[b][4])
                period_b.append(person_b[b][5] * 60 + person_b[b][6])

                # Make sure both visits start before they finish (validity)
                if period_a[0] < period_a[1] and period_b[0] < period_b[1]:
                        
                        # Check whether visit day is the same, and that
                        # visits are non-empty
                        if(person_a[a][2] == person_b[b][2] and
                                period_a[0] + period_a[1] > 0 and
                                period_b[0] + period_b[1] > 0):
                                
                            # Set the contact period's start to 
                            # Period A's and the end to Period B's end
                            overlap_start = period_a[0]
                            overlap_end = period_a[1]

                            # If Period B ends before A, set end to B's
                            if period_b[1] < period_a[1]:
                                overlap_end = period_b[1]

                            # IF Period B starts later, set start to B's
                            if (period_b[0] > period_a[0] and
                                    period_b[0] < period_a[1]):
                                overlap = True
                                overlap_start = period_b[0]

                            elif (period_b[0] < period_a[0] and
                                    period_b[1] > period_a[0]):
                                overlap = True

                            elif (period_b[0] == period_a[0] and 
                                    period_b[1] != period_a[1]):
                                overlap = True
                        
                        # If there is an overlap, create a contact 6-tuple:
                        # (Location, day, Start Hr, Start Min, End Hr, End Min)
                        if overlap:
                            result = (person_a[a][1],
                                      person_a[a][2],
                                      overlap_start // 60,
                                      overlap_start % 60,
                                      overlap_end // 60,
                                      overlap_end % 60)
                            
                            # Add the contact period's duration to the total
                            total += overlap_end - overlap_start
                            
                            # Add this contact period to the total set
                            overlap_set.add(result)
    
    total_formatted = (total // 60, total % 60)
    contact = (overlap_set, total_formatted)
    return contact

def forward_contact_trace(visits, index, day_time, second_order=False):
    '''
    Returns an alphabetically sorted list of first order contacts in the event
    of a community infection based on a database of visits and the date and
    time of a person's infection.
    '''
    # Firstly, initialise variables
    visits_dict = {}
    first_contacts = {}
    visits = sorted(visits)
    # Give names to values in day_time to make code more readable
    index_day = day_time[0]
    index_hour = day_time[1]
    index_minute = day_time[2]
    index_time = index_hour * 60 + index_minute
    
    # Add visits to a dictionary for each person
    for visit in range(len(visits)):
        person_index = visits[visit][0]
        if person_index in visits_dict:
            visits_dict[person_index].append(visits[visit])
        else:
            visits_dict[person_index] = [visits[visit]]
        
        # Initialise variables in the same format as before
        visit_day = visits[visit][2]
        visit_hour = visits[visit][5]
        visit_minute = visits[visit][6]
        visit_time = visit_hour * 60 + visit_minute
        # Remove visits before the infection
        if person_index == index:
            if visit_day < index_day:
                visits_dict[index].remove(visits[visit])
            elif (index_day == visit_day and 
                  visit_time < index_time):
                visits_dict[index].remove(visits[visit])
    
    for name in visits_dict:
        if name != index:
            if index in visits_dict:
                index_visits = visits_dict[index]
            # Compare each non-index visit to index ones after infection
            # to check for potential contact
            for entry in range(len(visits_dict[name])):
                    test_visit = [visits_dict[name][entry]]
                    if potential_contacts(test_visit, index_visits)[0]:
                        first_contacts[name] = visits_dict[name][entry]
    
    if second_order:
        # Move to a second function for second order tracing
        return second_order_contacts(first_contacts, visits, index)
    else:
        return sorted(list(first_contacts.keys()))
    
def second_order_contacts(first_contacts, visits, index):
    '''
    Called by the forward_contact_trace function to return an
    alphabetically sorted list of first and second order contacts
    in the case of a community infection.
    '''
    all_contacts = []

    for person in first_contacts:
        # Set variables to easily call the first function to get a first order
        # contract tracing of the previously found first contacts
        new_index = person
        day = first_contacts[person][2]
        hour = first_contacts[person][3]
        minute = first_contacts[person][4]
        day_time = (day, hour, minute)
        second_trace = forward_contact_trace(visits, new_index, day_time)
        
        for x in range(len(second_trace)):
            # Add second order contacts to the list of outputs but we make sure
            # to not include the original infected member
            if second_trace[x] != index:
                all_contacts.append(second_trace[x])
    from reference import potential_contacts

def backward_contact_trace(visits, index, day_time, window):
    '''
    Returns an alphabetically sorted list of backward contact traces in order
    to find potential sources of infection.
    '''
    # Firstly, initialise variables
    visits_dict = {}
    visits_in_window = []
    backward_contacts = []
    # Give names to values in day_time to make code more readable
    index_date = day_time[0]
    index_hour = day_time[1]
    index_min = day_time[2]
    index_time = index_hour * 60 + index_min
    
    # Create a dictionary of visits with each person as the key
    for visit in range(len(visits)):
        person_index = visits[visit][0]
        if person_index in visits_dict:
            visits_dict[person_index].append(visits[visit])
        else: 
            visits_dict[person_index] = [visits[visit]]
    
    # Remove the visits of the detected case as will interfere later
    if index in visits_dict:
        visits_dict.pop(index)
    
    # Thirdly, we need to find visits made by the infected person in
    # each day of the window
    for day in range(index_date + 1 - window, index_date + 1):
        for visit in range(len(visits)):
            # Initialise variables in the same format as before
            visit_person = visits[visit][0]
            visit_date = visits[visit][2]
            visit_hour = visits[visit][3]
            visit_min = visits[visit][4]
            visit_time = visit_hour * 60 + visit_min
            if index == visit_person:
                # Store list of visits that took place on the same day BEFORE
                # the infection
                if index_date == visit_date and visit_time <= index_time:
                    if visits[visit] not in visits_in_window:
                        visits_in_window.append(visits[visit])
                # Also add visits on the previous days in the window
                if day == visit_date:
                    if visits[visit] not in visits_in_window:
                        visits_in_window.append(visits[visit])

    # Lastly, test the index's visits against those in the dictionary
    # to find potential backward contacts/sources of infection
    for name in visits_dict:
        if name != index:
            # Test each visit in the dictionary to see if there is a 
            # potential contact with index visits in the set window
            for entry in range(len(visits_dict[name])):
                test_infection = [visits_dict[name][entry]]
                if potential_contacts(visits_in_window, test_infection)[0]:
                    backward_contacts.append(name)

    return sorted(backward_contacts)
    # Add first contacts to output and convert to set to remove
    # any potential duplicate names
    if first_contacts:
        all_contacts += first_contacts.keys()
        all_contacts = list(set(all_contacts))
    
    return sorted(all_contacts)

def backward_contact_trace(visits, index, day_time, window):
    '''
    Returns an alphabetically sorted list of backward contact traces in order
    to find potential sources of infection.
    '''
    # Firstly, initialise variables
    visits_dict = {}
    visits_in_window = []
    backward_contacts = []
    # Give names to values in day_time to make code more readable
    index_date = day_time[0]
    index_hour = day_time[1]
    index_min = day_time[2]
    index_time = index_hour * 60 + index_min
    
    # Create a dictionary of visits with each person as the key
    for visit in range(len(visits)):
        person_index = visits[visit][0]
        if person_index in visits_dict:
            visits_dict[person_index].append(visits[visit])
        else: 
            visits_dict[person_index] = [visits[visit]]
    
    # Remove the visits of the detected case as will interfere later
    if index in visits_dict:
        visits_dict.pop(index)
    
    # Thirdly, we need to find visits made by the infected person in
    # each day of the window
    for day in range(index_date + 1 - window, index_date + 1):
        for visit in range(len(visits)):
            # Initialise variables in the same format as before
            visit_person = visits[visit][0]
            visit_date = visits[visit][2]
            visit_hour = visits[visit][3]
            visit_min = visits[visit][4]
            visit_time = visit_hour * 60 + visit_min
            if index == visit_person:
                # Store list of visits that took place on the same day BEFORE
                # the infection
                if index_date == visit_date and visit_time <= index_time:
                    if visits[visit] not in visits_in_window:
                        visits_in_window.append(visits[visit])
                # Also add visits on the previous days in the window
                if day == visit_date:
                    if visits[visit] not in visits_in_window:
                        visits_in_window.append(visits[visit])

    # Lastly, test the index's visits against those in the dictionary
    # to find potential backward contacts/sources of infection
    for name in visits_dict:
        if name != index:
            # Test each visit in the dictionary to see if there is a 
            # potential contact with index visits in the set window
            for entry in range(len(visits_dict[name])):
                test_infection = [visits_dict[name][entry]]
                if potential_contacts(visits_in_window, test_infection)[0]:
                    backward_contacts.append(name)

    return sorted(backward_contacts)
