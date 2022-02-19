def training (miles_run, squats_performed):
    training = miles_run + squats_performed
    print (f"I have run {miles_run} miles!")
    print (f"I have done {squats_performed} squats!")
    print (f"I have done {training} training! \n")

training (5,10)
training (5+1, 10+1)

miles = 20
squats = 50
training (miles, squats)
training (miles + 20, squats + 50)

training (input("how many miles did you run \n"), input("how many squats did you do \n"))
