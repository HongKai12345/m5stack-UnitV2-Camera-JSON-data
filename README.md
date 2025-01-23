**INTRODUCTION**

This python script retrieves the JSON data being displayed on the M5Stack Camera UnitV2 website, stores it in the data variable and displays the information in the terminal. 

Hence, this eliminates the use of requiring a HY2.0-4P cable in order to receive the JSON data through the M5Stack Camera UnitV2 serial port and instead, retrieving the JSON data wirelessly.


**USE CASE:**

1)IOT (For sending JSON data over MQTT)

2)Data analysis (JSON data retrieved to be converted into Pandas DataFrame)


**PREREQUISITES**

pip install requests-html
