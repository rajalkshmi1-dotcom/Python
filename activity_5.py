#create variables and passenger details

passenger_age = 25
ticket_confirmed = True


#logical opeartors

if passenger_age >= 18 and ticket_confirmed:
    print("passenger eligble for travel")
    
#create seat availabilty variables
confirmed_seat = False
rac_seat = True

if confirmed_seat or rac_seat:
    print("reseravation available")

#create cancellation status variable
ticket_cancelled = False

if not ticket_cancelled:
    print("ticket is active")
#apply reservation rules for senior citizen
passenger_age = 65
payment_completed = True


if passenger_age >= 60 and payment_completed:
     print("senior citizen reservation approved")


#build ticket confirmation system

available_seats = 5
payment_status = True

if available_seats > 0 and payment_status:
    print("Ticket confirmed successfully")
else:
    print("Reservation Failed")

#check passenger eligibility for tatkal booking
    
valid_id_proof = True
booking_time_valid = True

if valid_id_proof and booking_time_valid:
   print("Tatkal Booking Allowed")
else:
    print("Tatkal Booking Denied")
    


          
    
    

    
    

    
    
