train = {
    "Train_Number": 12951,
    "Train_Number": "Mumbai Rajdhani Express",
    "source": "Mumbai",
    "Destination": "Delhi",
    "Available_Seats": 120
}
print("Train Information:")
print(train)

print("\nTrain Number:", train["Train_Number"])
print("Train Number:", train["Train_Number"])
print("source station:", train["source"])
print("Destination station:", train["Destination"])
print("Available Seats:", train["Available_Seats"])
                               
train = {
    "Train_Number": 12951,
    "Train_Name": "Mumbai Rajdhani Express",
    "Available_Seats": 120
}
print(train)
print("Train Name:", train["Train_Name"])
print("Available Seats:", train["Available_Seats"])
train["Available_Seats"] = 95
print(train)
train.update({"Platform": 4})
print(train)
train.pop("Platform")
print(train)
print("\nUpdated Train Record:")
print(train)


