from pyproj import Proj

#とりあえず縮尺の確認

#UTMの座標系
#An arbitral point in EQA coordinate
#芝浦工業大学交差点
lon_1=139.648076  #[deg.]
lat_1=35.952118 #[deg.]
#任意の一点
lon_2=139.650576  #[deg.]
lat_2=35.950717  #[deg.]

##Compute UTM zone
#"int": Extract only integer value
#31: Offset for UTM zone definition
#6: Angle in a UTM zone for the longitude direction
e2u_zone=int(divmod(lon_1, 6)[0])+31

#Define EQA2UTM converter
e2u_conv=Proj(proj='utm', zone=e2u_zone, ellps='WGS84')

#Apply the converter
utmx_1, utmy_1=e2u_conv(lon_1, lat_1)
utmx_2, utmy_2=e2u_conv(lon_2, lat_2)

#Add offset if the point in the southern hemisphere
if lat_1<0:
    utmy_1=utmy_1+10000000

if lat_2<0:
    utmy_2=utmy_2+10000000

print(" UTM zone is ", e2u_zone, " \n", \
      "UTM Easting is", utmx_1, "[m]\n",\
      "UTM Northing is ", utmy_1, "[m]")
print("\n")
print(" UTM zone is ", e2u_zone, " \n", \
      "UTM Easting is", utmx_2, "[m]\n",\
      "UTM Northing is ", utmy_2, "[m]")
print("\n")

dx_utm = abs(utmx_2 - utmx_1)
dy_utm = abs(utmy_2 - utmy_1)

print("x difference is ",dx_utm)
print("y difference is ",dy_utm,"\n")

#UnrealEngineの座標系
#芝浦工業大学交差点
x_unreal_1 = -91.102
y_unreal_1 = -95.103

#任意の点
x_unreal_2 = 135.492
y_unreal_2 = 60.038

#RoadRunnerの座標
#芝浦工業大学交差点
x_RoadRunner_1 = -91.102
y_RoadRunner_1 = 95.103

dx_unreal = abs(x_unreal_2 - x_unreal_1)
dy_unreal = abs(y_unreal_2 - y_unreal_1)

print("x difference is ",dx_unreal)
print("y difference is ",dy_unreal,"\n")


#座標の縮尺に差がないことがわかった
#縮尺が同じ→座標だけ移動させた位置が原点
#(0,0)のUTMと与えられた位置情報のUTMを比較して任意の座標を決定することができる！

#RoadRunnerの座標とy座標だけ反転してるから
#RoadRunnerの座標に変換したあとにマイナスをつけるのが良さそう

#(0,0)の座標を求めていく　※確認用
utmx_0 = utmx_1 - x_RoadRunner_1
utmy_0 = utmy_1 - y_RoadRunner_1

e2u_conv=Proj(proj='utm', zone=e2u_zone, ellps='WGS84')
lon,lat = e2u_conv(utmx_0, utmy_0, inverse=True)

print("Longitude is ",lon," [deg.]")
print("Latitude is ", lat, "[deg.]")

#(0,0)の座標