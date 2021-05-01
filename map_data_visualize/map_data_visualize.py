import mapboxgl
from mapboxgl.utils import create_color_stops
from mapboxgl.viz import*
import json
from IPython.display import IFrame
mapboxgl.__version__

geo_data = '/Users/heechankang/Desktop/pythonworkspace/map_data_visualize/data/older_seoul.geojson'

# 파이썬으로 파일 읽기

with open(geo_data) as f:
    data = json.loads(f.read())

from mapboxgl.utils import create_color_stops

# 환경변수에서 자신의 mapbox token 가져오기
# 내꺼
# token = 'pk.eyJ1IjoiaGVlY2hhbmthbmciLCJhIjoiY2tuZTB6ZGc1MDJwaDJvbnczM3RiMWJvdiJ9.pO54Xq5V1Sv2S8PMR5jfVw'
token = 'pk.eyJ1IjoianloOTUxIiwiYSI6ImNraWQ4eWE2ajFjZ2gyd212Nmw3ZzM1YmcifQ.VTEqIgStpmZiLNRakB_mlQ'
# 서울 중심부 경도, 위도
center = [126.986, 37.565]

color_breaks = [0, 10000, 20000, 30000, 40000, 50000]
color_stops = create_color_stops(color_breaks, colors='BuPu')
# color_stops 에는 아래 값 들어감
# color_stops = [
#     [0, 'rgb(237,248,251)'],
#     [10000, 'rgb(191,211,230)'],
#     [20000, 'rgb(158,188,218)'],
#     [30000, 'rgb(140,150,198)'],
#     [40000, 'rgb(136,86,167)'],
#     [50000, 'rgb(129,15,124)']
# ]

# ChoroplethViz 를 그립니다.
viz = ChoroplethViz(
    access_token=token,
    data=data,
    color_property='인구',
    color_stops=color_stops,
    center = center,
    zoom=10
)

# 맵 출력
viz.show()

#####################################

from mapboxgl.utils import create_numeric_stops

viz.bearing = -15
viz.pitch = 45

viz.height_property = '인구'

numeric_stops = create_numeric_stops([0, 10000, 20000, 30000, 40000, 50000], 0, 3000)

viz.height_stops = numeric_stops
viz.height_function_type = 'interpolate'

viz.show()

########################

match_color_stops = [
    ['양재 1동', 'rgb(46, 204, 113)'],
    ['세곡동', 'rgb(231, 76, 60)'],
    ['역삼1동', 'rgb(142, 68, 173)']
]

token = 'pk.eyJ1IjoianloOTUxIiwiYSI6ImNraWQ4eWE2ajFjZ2gyd212Nmw3ZzM1YmcifQ.VTEqIgStpmZiLNRakB_mlQ'
center = [126.986, 37.565]

viz = ChoroplethViz(
    data,
    access_token=token,
    color_function_type = 'match',
    color_property = "동",
    color_stops=match_color_stops,
    color_default='rgba(52,73, 94, 0.5)',
    center=center,
    bearing=-15,
    pitch = 45,
    zoom = 10)
viz.show()

############################

# 4. csv

import pandas as pd

df = pd.read_csv('/Users/heechankang/Desktop/pythonworkspace/map_data_visualize/data/toilet_seoul.csv')
df.head()

from mapboxgl.utils import df_to_geojson

geo_data = df_to_geojson(
    df=df,
    lat='위도',
    lon='경도',
    #filename = "data/toilet_seoul.geojson"
    # 파일 저장 시 위 주석 해제
)

type(geo_data)

################################

geo_data = 'map_data_visualize/data/toilet_seoul.geojson'
from mapboxgl.viz import*
import json
with open(geo_data, encoding='utf-8') as f:
    data = json.loads(f.read())

token = 'pk.eyJ1IjoianloOTUxIiwiYSI6ImNraWQ4eWE2ajFjZ2gyd212Nmw3ZzM1YmcifQ.VTEqIgStpmZiLNRakB_mlQ'
center = [126.986, 37.565]

viz = CircleViz(
    data,
    access_token=token,
    center = center,
    zoom = 10
)

viz.show()

###########################
# 이용량에 따라 색 입력
viz.color_property = '\uace0\uc720\ubc88\ud638'
viz.color_stops = create_color_stops([0, 100, 200, 300, 400, 500], colors = 'BuPu')

viz.show()

#############################

from mapboxgl.utils import(
    create_color_stops,
    create_radius_stops
)

token = 'pk.eyJ1IjoianloOTUxIiwiYSI6ImNraWQ4eWE2ajFjZ2gyd212Nmw3ZzM1YmcifQ.VTEqIgStpmZiLNRakB_mlQ'
center = [126.986, 37.565]
viz = GraduatedCircleViz(
    data,
    access_token = token,
    color_property= '이용량',
    color_stops=create_color_stops([0, 100, 200, 300, 400, 500], colors= 'BuPu'),
    radius_property="이용량",
    radius_stops=create_radius_stops([0, 100, 200, 300, 400,500], 0, 8),
    center = center,
    zoom = 10
)

viz.show()


###############################

# HeatMapViz

from mapboxgl.utils import (
    create_numeric_stops,
    create_color_stops
)

token = 'pk.eyJ1IjoianloOTUxIiwiYSI6ImNraWQ4eWE2ajFjZ2gyd212Nmw3ZzM1YmcifQ.VTEqIgStpmZiLNRakB_mlQ'

center = [126.986, 37.565]
viz = HeatmapViz(
    data,
    access_token = token,
    weight_property='이용량',
    weight_stops=create_numeric_stops([100, 200, 300, 400, 500], 0, 1),
    color_stops=create_color_stops([0.1, 0.3, 0.5, 0.7, 0.9], colors='BuPu'),
    radius_stops=create_numeric_stops([8, 10, 12, 14, 16], 3, 12),
    center = center,
    zoom = 10
) 

viz.show()

###############################
# Clustered CircleViz

from mapboxgl.utils import(
    create_color_stops,
    create_radius_stops
)

token = 'pk.eyJ1IjoianloOTUxIiwiYSI6ImNraWQ4eWE2ajFjZ2gyd212Nmw3ZzM1YmcifQ.VTEqIgStpmZiLNRakB_mlQ'
center = [126.986, 37.565]

viz = ClusteredCircleViz(
    data,
    access_token=token,
    color_stops=create_color_stops([100, 200, 300, 400, 500, 1000], colors='BuPu'),
    radius_stops=create_radius_stops([100, 200, 300, 400, 500, 1000],0, 30),
    cluster_radius=60,
    center = center,
    zoom = 10
)

viz.show()

###############################

import json

with open('/Users/heechankang/Desktop/pythonworkspace/map_data_visualize/data/dongjak_road.geojson') as f:
    data = json.loads(f.read())


from mapboxgl.utils import(
    create_color_stops,
    create_numeric_stops
)


token = 'pk.eyJ1IjoianloOTUxIiwiYSI6ImNraWQ4eWE2ajFjZ2gyd212Nmw3ZzM1YmcifQ.VTEqIgStpmZiLNRakB_mlQ'
center = [126.986, 37.565]

viz = LinestringViz(
    data,
    access_token=token,
    color_property='도로폭',
    color_stops=create_color_stops([10, 15,20,25,30,35,40,45,50], colors='BuPu'),
    line_width_property='도로폭',
    line_width_stops=create_numeric_stops([10, 15,20,25,30,35,40,45,50], 1, 4),
    center = center,
    zoom = 12

)


viz.show()

