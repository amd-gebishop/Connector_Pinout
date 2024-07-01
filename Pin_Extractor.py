import os
# Read in netlist
# Parse netlist for reference designators

NETLIST_FILE = "dialcnet.dat"
REFERNCE_DESIGNATOR = "CONN1"
OUTPUT_CSV_FILE = REFERNCE_DESIGNATOR + "_PINLIST.csv"

# Delete previous output files
if os.path.isfile(OUTPUT_CSV_FILE) == True:
    os.remove(OUTPUT_CSV_FILE)

# Create a list of all nets connected to REFERENCE_DESIGNATOR
Connectivity = {}
NetlistFile = open(NETLIST_FILE, "r")
FirstLine = True
PinCount = 0
for line in NetlistFile:
    if FirstLine == True:
        FirstLine = False
        continue
    if line.strip() == "END CONCISE NET LIST":
        continue
    Net = line.split()[0]
    Reference_Designator = line.split()[1]
    Pin = line.split()[2]
    if REFERNCE_DESIGNATOR == Reference_Designator:
        PinCount = PinCount + 1
        Connectivity[Pin] = Net

print ("Found " + str(PinCount) + " pins")

# Create output files
OutputCSVFile = open(OUTPUT_CSV_FILE, "w")
OutputCSVFile.write("Pin,Net Name\n")
for pin in Connectivity:
    if Connectivity[pin][0] == '+':
        OutputCSVFile.write(pin + ",'" + Connectivity[pin] + "\n")
    else:
        OutputCSVFile.write(pin + "," + Connectivity[pin] + "\n")
OutputCSVFile.close()

NetlistFile.close()