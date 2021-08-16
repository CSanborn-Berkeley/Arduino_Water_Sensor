from Arduino import Arduino
from Arduino import WaterSensor

#########################################
# EDIT THESE AS THE USER                #
#########################################
name = "Test Sensor"
emails = ["csanborn@berkeley.edu"]


##########################################
# DO NOT EDIT THESE                      #
##########################################
password = input("Enter email password: ")
print("Starting Sensor")
mysensor = WaterSensor(name,emails,password,9600,portname="COM4")
mysensor.listen()
