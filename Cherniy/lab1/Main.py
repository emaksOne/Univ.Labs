import Contour
import Process
from Simple import Point
from IO import Reader
from Plot import Core as pl
from Utils import Utils

list_of_points = Point.CreateListOfPoints(Reader.contour_points)
contour = Contour.Contour(Utils.createContour())
init_flow_len = Reader.init_flow_len
x_max = Reader.x_max
y_max = Reader.y_max
alfa = Reader.alfa
circulation = Reader.circulation





process = Process.Process(contour, x_max, y_max, init_flow_len, circulation, alfa)



pl.drawField(Utils.parseField(process.vector_field), Utils.parseContour(contour.list_of_vortex), process.pressure_diff, process.pressure_max, process.pressure_min)






