#import plotly.plotly
import plotly.plotly as py
import plotly.graph_objs as go



def drawField(field, contour, pressure_field, pressure_max, pressure_min):
    #plotly.tools.set_credentials_file(username='emaksOne', api_key='u5pjmbf7gy')
    trace = go.Scatter()
    data = [trace]
    shapes = []
    for line in field:
        temp = {
            'type': 'line',
            'x0': line['x0'],
            'y0': line['y0'],
            'x1': line['x1'],
            'y1': line['y1'],
            'line':{
                'color': 'Blue',
                'width': 2,
            }
        }
        shapes.append(temp)
    for line in contour:
        temp = {
            'type': 'line',
            'x0': line['x0'],
            'y0': line['y0'],
            'x1': line['x1'],
            'y1': line['y1'],
            'line': {
                'color': 'Red',
                'width': 3,
            }
        }
        shapes.append(temp)

    layout = {
        'xaxis': {
            'range': [0, 50]
        },
        'yaxis': {
            'range': [0, 50]
        },
        'shapes': shapes
    }
    step = (pressure_max - pressure_min) / 16.0
    contour_trace = go.Contour(z=pressure_field,
                   autocontour=False,
                   colorscale='Greens',
                   contours=dict(
                       start=pressure_min,
                       end=pressure_max,
                       size=step,
                   ),
                   )


    data.append(contour_trace)
    fig = {
        'data': data,
        'layout': layout
    }



    py.plot(fig, filename='field')

