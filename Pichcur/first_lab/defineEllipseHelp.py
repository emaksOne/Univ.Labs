from __future__ import division
import numpy as np

def initEllipse():
    #init ellipse (M0)
    ellipseCenter = [2, 4, 0]
    N = 3


    semiAxes = [3, 1, 2]

    eigenValues = [
        [
            (0 if j != i else 1 / semiAxes[i] ** 2) for j in range(N)
            ]
        for i in range(N)
        ]

    vec1 = [1, 0, 0]
    vec2 = [0, 1, 0]
    vec3 = [0, 0, 1]

    eigenVectorsMatrix = np.transpose([vec1, vec2, vec3])
    eigenVectorsMatrixInv = np.linalg.inv(eigenVectorsMatrix)

    ellipse = np.dot(eigenVectorsMatrix, eigenValues)
    ellipse = np.dot(ellipse, eigenVectorsMatrixInv)

    return ellipse, ellipseCenter

def initEllipseByQuadraticEquatin():
    ellipseCenter = [1, 1, 1]

    b11 = 5
    b22 = 5

    b12 = -2
    b21 = b12
    test_m = [[b11, b12],
              [b21, b22]]
    vals, vects = np.linalg.eig(test_m)
    dot = np.dot(vects[0], vects[1])
    print(vals, vects, dot)

    a11 = 4
    a22 = 9
    a33 = 1

    a12 = 2*0.05
    a13 = 2*0.01

    a21 = a12
    a23 = 2*0.1

    a31 = a13
    a32 = a23

    quad_m = [[a11**0.5, a12/2, a13/2],
              [a21/2, a22**0.5, a23/2],
              [a31/2, a32/2, a33**0.5]]
    #quad_m = np.linalg.inv(quad_m)
    eig_vals, eig_vec = np.linalg.eig(quad_m)

    print(eig_vals, eig_vec)

    return quad_m, ellipseCenter