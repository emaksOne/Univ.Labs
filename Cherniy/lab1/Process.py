from Simple import Vector
from Simple import VectorField
from Simple import Point
from Simple import Normal
from Mathematics.SystemOfEquation import SolveSystem
import math as mt
import numpy as np


class Process:
    def __init__(self, contour, x_max, y_max, init_flow_len, circulation, alfa):
        self.alfa = alfa
        self.x_max = x_max
        self.y_max = y_max
        self.initFlow = Vector.Vector(init_flow_len * mt.cos(alfa), init_flow_len * mt.sin(alfa))
        self.circulation = circulation
        self.contour = contour
        self.vertex_intesities = self.FindVertexIntesities()
        print('intensities = {0}'.format(self.vertex_intesities))
        self.vector_field = self.GetVectorField()
        self.pressure_diff = self.GetPressureDiffField()
        self.scale = self.initPressureScale()
        self.pressure_max = self.GetPressureMax()
        self.pressure_min = self.GetPressureMin()

    def FindVertexIntesities(self):
        matrixA = self.InitCoefMatrix(self.contour.list_of_callocation_points, self.contour.list_of_vortex)
        matrixB = self.InitDependentVars(self.contour.list_of_vortex, self.initFlow, self.circulation)

        intensities = SolveSystem.SolveSystem(matrixA, matrixB)
        return intensities

    def GeneralVectorFieldInThePoint(self, point):
        vector = Vector.Vector()
        for i in range(0, len(self.contour.list_of_vortex)):
            vector += self.vertex_intesities[i] * VectorField.VectorField(point, self.contour.list_of_vortex[i])
        vector += self.initFlow
        return vector

    def PressureDiffInThePoint(self, point):

        cp = 1 - self.GeneralVectorFieldInThePoint(point) * self.GeneralVectorFieldInThePoint(point) / \
                 (self.initFlow * self.initFlow)
        return cp

    def GetVectorField(self):
        field = []
        for i in range(0, self.x_max+1):
            field.append([])
            for j in range(0, self.y_max+1):
                point = Point.Point(i, j)
                vector = self.GeneralVectorFieldInThePoint(point)
                #print("point = ({0})   vector=({1})".format(point, vector))
                field[i].append(vector)
        return field

    def GetPressureDiffField(self):
        field = []
        for i in range(0, self.x_max+1):
            field.append([])
            for j in range(0, self.y_max+1):
                point = Point.Point(i, j)
                vector = self.PressureDiffInThePoint(point)
                field[i].append(vector)
        return field

    def InitCoefMatrix(self, list_of_callocation_points, list_of_vertex):
        coef = []
        for k in range(0, len(list_of_vertex)):
            coef.append([])
            for j in range(0, len(list_of_vertex)):
                if(k == len(list_of_callocation_points)):
                    coef[k].append(1)
                else:
                    callocation_point = list_of_callocation_points[k]
                    temp = VectorField.VectorField(callocation_point, list_of_vertex[j])
                    temp *= Normal.Normal(list_of_vertex[k], list_of_vertex[k+1])
                    coef[k].append(temp)
        return coef

    def InitDependentVars(self, list_of_vertex, initField, circulation):
        b = []
        for k in range(0, len(list_of_vertex) - 1):
            normal = Normal.Normal(list_of_vertex[k], list_of_vertex[k + 1])
            temp = initField.x * mt.cos(self.alfa) * normal.x + initField.y * mt.sin(self.alfa) * normal.y
            temp *= (-1)
            b.append(temp)
        b.append(circulation)
        return b

    def isContour(self, point):
        for p in self.contour.list_of_vortex:
            if point == p:
                return True
        return False

    def initPressureScale(self):
        pressure = []
        for i in range(0, len(self.pressure_diff)):
            for j in range(0, len(self.pressure_diff[0])):
                pressure.append(self.pressure_diff[i][j])
        pressure.sort()
        scale = np.linspace(pressure[0], pressure[-1], 17)
        return scale

    def GetPressureMax(self):
        x = np.matrix(self.pressure_diff)
        max = x.max()
        return max

    def GetPressureMin(self):
        x = np.matrix(self.pressure_diff)
        min = x.min()
        return min