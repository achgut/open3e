# Open3E interface

* Connects E3 boiler (vcal or vdens) controller through CAN UDS or doip
* Read known datapoints
* Listen to commands on mqtt
* Experimental (!) write support (untested)

# Requirements
For a fresh Raspberry PI install git, python3 and python-pip first:

    sudo apt install git python3 python3-pip  
  
Now clone this repository to your system:  

    git clone https://github.com/abnoname/open3e.git  
      
Change into the directory

    cd open3e
      
Eventually run:
  
    pip3 install -r requirements.txt  

If you get the error "error: externally-managed-environment" you could add *--break-system-packages* to the preveious command.<br>
(please see: https://stackoverflow.com/questions/75608323/how-do-i-solve-error-externally-managed-environment-every-time-i-use-pip-3)  

# Setup CAN Bus
    sudo ip link set can0 up type can bitrate 250000

# Usage
    usage: Open3Eclient.py [-h] [-c CAN] [-d DOIP] [-dev DEV] [-a] [-r READ] [-raw] [-w WRITE] [-t TIMESTEP] [-m MQTT] [-mfstr MQTTFORMATSTRING] [-muser MQTTUSER]
                           [-mpass MQTTPASS] [-j] [-v] [-l CMND-TOPIC]

    options:
    -h, --help              show this help message and exit
    -c CAN, --can CAN       use can device, e.g. can0
    -d DOIP, --doip DOIP    use doip access, e.g. 192.168.1.1
    -dev DEV, --dev DEV     boiler type --dev vdens or --dev vcal || pv/battery --dev vx3, --dev vair
    -a, --scanall           dump all dids
    -r READ, --read READ    read did, e.g. 0x173,0x174
    -raw, --raw             return raw data for all dids
    -w WRITE, --write WRITE
                            write did, e.g. -w 396=D601 (raw data only!)
    -t TIMESTEP, --timestep TIMESTEP
                            read continuous with delay in s
    -m MQTT, --mqtt MQTT  publish to server, e.g. 192.168.0.1:1883:topicname
    -mfstr MQTTFORMATSTRING, --mqttformatstring MQTTFORMATSTRING
                            mqtt formatstring e.g. {ecuAddr:X}_{device}_{didNumber}_{didName}
                            ':X' is optional and sets Format of ECU address. may be X, x, d, ...
    -muser MQTTUSER, --mqttuser MQTTUSER
                            mqtt username
    -mpass MQTTPASS, --mqttpass MQTTPASS
                            mqtt password
	-j, --json          send JSON structure via MQTT
    -v, --verbose		verbose info
	-l, --listen		mqtt topic to listen for commands, e.g. open3e/cmnd

# Read dids
    python3 Open3Eclient.py -c can0 -dev vdens -r 268 -v
    0x10c FlowTempSensor 27.2

    python3 Open3Eclient.py -c can0 -dev vcal -r 318 -v
    0x13e WaterPressureSensor 1.8

    python3 Open3Eclient.py -c can0 -dev vcal -r 377 -v
    0x179 IdentNumber XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    python3 Open3Eclient.py -c can0 -dev vcal -r 1043 -v
    0x413 FlowMeterSensor 2412.0

    python3 Open3Eclient.py -c can0 -dev vx3 -r 1664 -v
    1664 ElectricalEnergyStorageStateOfCharge 44

# Interval Readout
    python3 Open3Eclient.py -c can0 -dev vcal -r 1043 -t 1
    2412.0
    2413.0
    2411.0
    2412.0
    ...

# Write did (experimental)
    python3 Open3Eclient.py -c can0 -dev vdens -raw -w 396=D601
    -> sets domestic hot water setpoint to 47degC

# Publish datapoints to mqtt
    python3 Open3Eclient.py -c can0 -dev vcal -r 268,269,271,274,318,1043 -m 192.168.0.5:1883:open3e -t 1
    -> will periodically scan datapoints and publish data to broker 192.168.0.5

    python3 Open3Eclient.py -c can0 -dev vcal -r 268,269,271,274,318,1043 -m 192.168.0.5:1883:open3e -t 1 -mfstr "{didNumber}_{didName}"
    -> will publish with custom identifier format: e.g. open3e/268_FlowTemperatureSensor

# Listener mode
    python3 Open3Eclient.py -c can0 -dev vcal -m 192.168.0.5:1883:open3e -mfstr "{didNumber}_{didName}" -l open3e/cmnd
    
    will listen for commands on topic open3e/cmnd with payload in json format:
<<<<<<< HEAD
    {"mode": "read"|"read-json"|"read-raw"|"write"|"write-raw", "data":[list of data]}
=======
    {"mode":"read"|"write"|"write-raw", "data":[list of data], "addr":"ECU_addr"} 
    rem: "addr" is optional, otherwise defaut ECU address used
>>>>>>> feat-classmulti
    
    to read dids 271 and 274:
    {"mode": "read", "data":[271,274]}
    
    to read dids 265 and 266 as JSON-objects (even w/o option -json):
    {"mode": "read-json", "data":[265,266]}
    
    to read dids 265 and 266 as raw data (even w/o option -raw):
    {"mode": "read-raw", "data":[265,266]}
    
    to write value of 45.0 to did 396 and value of 21.5 to did 424:
    {"mode": "write", "data":[[396,45.0],[424,21.5]]}

    to set frost protect threshold to -9°C in complex did
    (A6FF lsb..msb -> 0xFFA6 -> -90 -> -9.0°C; Byte 0 unchanged):
    {"mode": "write-raw", "data":[[2855,"01A6FF"]]}

    to set frost protect threshold and eco function threshold to -9°C (complex dids):
    {"mode": "write-raw", "data":[[2855,"01A6FF"],[2426,"01A6FF000A00"]]}

 
    Option -m is mandatory for this mode.
    Options -r, -t, -j, -v may be used in parallel.
    
