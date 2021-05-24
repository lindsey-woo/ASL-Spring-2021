### parseGPS.py

Parses rosbag data and extracts the /navsat/fix topic, outputting lattitude and longitutde coordinates in a csv file

### plotGPS.py

Plots lattitude and longitutde coordinates overlaid on Google Maps

To plot GPS data from jackal, run the parseGPS.py script with a rosbag

To plot GPS data from the Atlas, extract the P1 data log from the Atlas GUI and run the extract_position_data.py script from https://github.com/PointOneNav/fusion-engine-client.

### plotGPSsolution.py

Plots GPS solution type. 
![Image of GPS](https://github.com/lindsey-woo/ASL-Spring-2021/blob/main/GPS/images/GPS%20solution.JPG)
