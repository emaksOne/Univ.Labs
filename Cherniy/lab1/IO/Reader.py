import json


with open('data.json') as data_file:
    data = json.load(data_file)

contour_points = data["contour_points"]
x_max = data["x_max"]
y_max = data["y_max"]
init_flow_len = data["init_flow_len"]
alfa = data["alfa"]
circulation = data["circulation"]