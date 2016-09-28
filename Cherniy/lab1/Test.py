import plotly.plotly
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='emaksOne', api_key='u5pjmbf7gy')
data = go.Data([
    go.Contour(
        z=[[10, 10.625, 12.5, 15.625, 20],
           [5.625, 6.25, 8.125, 11.25, 15.625],
           [2.5, 3.125, 5., 8.125, 12.5],
           [0.625, 1.25, 3.125, 6.25, 10.625],
           [0, 0.625, 2.5, 5.625, 10]]
    )
])
py.plot(data)
# py.plot([{
#     'z': [
#         [0, 1, 2, 3, 4, 5, 6, 7]
#     ],
#     'type': 'heatmap',
#     'colorscale': [
#         # Let first 10% (0.1) of the values have color rgb(0, 0, 0)
#         [0, 'rgb(0, 0, 0)'],
#         [0.1, 'rgb(20, 20, 20)'],
#
#         # Let values between 10-20% of the min and max of z
#         # have color rgb(20, 20, 20)
#         [0.1, 'rgb(20, 20, 20)'],
#         [0.2, 'rgb(20, 20, 20)'],
#
#         # Values between 20-30% of the min and max of z
#         # have color rgb(40, 40, 40)
#         [0.2, 'rgb(40, 40, 40)'],
#         [0.3, 'rgb(40, 40, 40)'],
#
#         [0.3, 'rgb(60, 60, 60)'],
#         [0.4, 'rgb(60, 60, 60)'],
#
#         [0.4, 'rgb(80, 80, 80)'],
#         [0.5, 'rgb(80, 80, 80)'],
#
#         [0.5, 'rgb(100, 100, 100)'],
#         [0.6, 'rgb(100, 100, 100)'],
#
#         [0.6, 'rgb(120, 120, 120)'],
#         [0.7, 'rgb(120, 120, 120)'],
#
#         [0.7, 'rgb(140, 140, 140)'],
#         [0.8, 'rgb(140, 140, 140)'],
#
#         [0.8, 'rgb(160, 160, 160)'],
#         [0.9, 'rgb(160, 160, 160)'],
#
#         [0.9, 'rgb(180, 180, 180)'],
#         [1.0, 'rgb(180, 180, 180)']
#     ],
#     'colorbar': {
#         'tick0': 0,
#         'dtick': 1
#     }
# }], filename='heatmap-discrete-colorscale')