passenger_name = "Rahul Sharma"
ticket_status = "Confirmed"


if ticket_status == "Confirmed":
    print("Ticket is Confirmed")
    
waiting_list = 3

if waiting_list == 0:
    print("Ticket Confirmed")
else:
    print("Ticket is in Waiting List")
    
ticket_status = "rac"


if ticket_status == "confirmed":
    print("seat allocated successfully")
elif ticket_status == "rac":
    print("partial reservation available")
else:
    print("ticket is in waitng list")

age = 65
if age >= 60:
    print("Passenger Eligible for Senior Citizen Discount")
 	
 	
age = 65
is_ticket_confirmed = True
if age >= 60 and is_ticket_confirmed == True:
    print("Passenger eligible for Senior Citizen Benefits")
    
ticket_status = "Confirmed"
payment_status = "Paid"

if ticket_status == "Confirmed" and payment_status == "Paid":
    print("Ticket Successfully Booked")
 	
elif ticket_status == "RAC":
    print("Partial Seat Reservation Available")
else:
    print("Booking Pending")

#build final resevation rule validation module

passenger_name = "Rajalakshmi"
passenger_age = 41
available_seats = 2
payment_completed = True
ticket_cancelled = False


if (
    passenger_age >= 18 and
    available_seats > 0 and
    payment_completed and
    not ticket_cancelled
):
    print("--------------------------------")
    print("Indian Railways Reservation")
    print("--------------------------------")
    print("pasenger name :", passenger_name)
    print("Reservation Status : confirmed")
else:
    print ("Reservation Failed")
    
    
    
	
