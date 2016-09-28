import numpy


def SolveSystem(matrix_A, matrix_B):
    res = numpy.linalg.solve(matrix_A, matrix_B)
    return res

# def SolveSystem(list_of_callocation_points, list_of_vertex, initField, circulation):
#
#     #solve system like Ax = B
#     matrix_A = InitCoefMatrix(list_of_callocation_points, list_of_vertex)   # [][]
#     matrix_B = InitDependentVars(list_of_vertex, initField, circulation)    # []
#     x = numpy.linalg.solve(matrix_A, matrix_B)
#     return x
#
# def InitCoefMatrix(list_of_callocation_points, list_of_vertex):
#     coef = []
#     for k in range(0, len(list_of_vertex) - 1):
#         coef.append([])
#         for j in range(0, len(list_of_vertex) - 1):
#             if j == len(list_of_vertex) - 1:
#                 coef[k].append(1)
#             else:
#                 callocation_point = list_of_callocation_points[j]
#                 temp = Process.Process.GeneralVectorFieldInThePoint(callocation_point, list_of_vertex[k])
#                 temp *= Process.Normal.Normal(callocation_point)
#                 coef[k].append(temp)
#
#     return coef
#
#
# def InitDependentVars(list_of_vertex, initField, circulation):
#     b = []
#     for k in range(0, len(list_of_vertex) - 2):
#         temp = Process.Normal.Normal(list_of_vertex[k], list_of_vertex[k+1])
#         temp *= initField
#         temp *= (-1)
#         b.append(temp)
#     b.append(circulation)
#    return b