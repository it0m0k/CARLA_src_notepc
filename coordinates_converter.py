from pyproj import Proj

#(0,0)の緯度/経度
#Longitude is  139.6491005155459  [deg.]
#Latitude is  35.951272162113824 [deg.]

Lon = 139.6491005155459
Lat = 35.951272162113824 

#任意の位置座標->書き換えれば通信で取得したり，ファイルから読み込んでこの変数に入れるだけ
Lon_1 = 139.648076 
Lat_1 = 35.952118

##Compute UTM zone
#"int": Extract only integer value
#31: Offset for UTM zone definition
#6: Angle in a UTM zone for the longitude direction
e2u_zone=int(divmod(Lon, 6)[0])+31
e2u_zone_1=int(divmod(Lon_1, 6)[0])+31

#Define EQA2UTM converter
e2u_conv=Proj(proj='utm', zone=e2u_zone, ellps='WGS84')
e2u_conv_1=Proj(proj='utm', zone=e2u_zone_1, ellps='WGS84')

#Apply the converter
utmx, utmy = e2u_conv(Lon, Lat)
utmx_1,utmy_1 = e2u_conv(Lon_1, Lat_1)

RoadRunner_x = utmx_1 - utmx
RoadRunner_y = utmy_1 - utmy

x = RoadRunner_x
y = -RoadRunner_y

print(x)
print(y)
