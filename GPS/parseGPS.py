import rosbag
from geometry_msgs.msg import Point
import pandas as pd
  
bag = rosbag.Bag('2021-05-14-14-22-40.bag')
topic = '/navsat/fix'
column_names = ['Latitude','Longitude']
df = pd.DataFrame(columns=column_names)
 
for topic, msg, t in bag.read_messages(topics=['/navsat/fix']):
    lat = msg.latitude
    long = msg.longitude
 
    df = df.append(
            {'Latitude': lat,
             'Longitude': long},
             ignore_index=True
    )
  
csvfile = 'out4.csv'
df.to_csv(csvfile)
