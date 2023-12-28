import numpy as np
from Detection import cvToolsCython


class mathUtils:
    

    @staticmethod
    def linear_regression(pts: np.ndarray):
        x = np.expand_dims(pts[:, 0], axis=-1)
        y = np.expand_dims(pts[:, 1], axis=-1)
        featurs = np.hstack((np.ones_like(x), x))  # , x**2))
        theta = np.linalg.inv(np.matmul(featurs.transpose(), featurs))
        theta = np.matmul(theta, featurs.transpose())
        theta = np.matmul(theta, y)
        slope = theta[1]
        intercept = theta[0]
        return slope, intercept
    
