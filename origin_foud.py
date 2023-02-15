from pyproj import Proj

#An arbitral point in EQA coordinate
#実空間の座標
#任意の緯度/経度（芝浦工業大学交差点の例）
lon_1=139.648076  #[deg.]
lat_1=35.952118 #[deg.]

#RoadRunnerの座標(shibaura_RoadRunner_5,6の時)
#0216時点で最新
#芝浦工業大学交差点
x_RoadRunner_1 = -74.807
y_RoadRunner_1 = 95.659

##Compute UTM zone
#"int": Extract only integer value
#31: Offset for UTM zone definition
#6: Angle in a UTM zone for the longitude direction
e2u_zone=int(divmod(lon_1, 6)[0])+31

#Define EQA2UTM converter
e2u_conv=Proj(proj='utm', zone=e2u_zone, ellps='WGS84')

#Apply the converter
utmx_1, utmy_1=e2u_conv(lon_1, lat_1)

#Add offset if the point in the southern hemisphere
if lat_1<0:
    utmy_1=utmy_1+10000000

#(0,0)の座標を求めていく　
utmx_0 = utmx_1 - x_RoadRunner_1
utmy_0 = utmy_1 - y_RoadRunner_1

print(utmx_0)
print(utmy_0)

e2u_conv=Proj(proj='utm', zone=e2u_zone, ellps='WGS84')
lon,lat = e2u_conv(utmx_0, utmy_0, inverse=True)

print("Longitude is ",lon," [deg.]")
print("Latitude is ", lat, "[deg.]")