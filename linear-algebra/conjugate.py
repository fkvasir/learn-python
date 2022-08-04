rom typing import Any

import numpy as np


def _is_matrix_spd(matrix: np.ndarray) -> bool:
    """
    Returns True if input matrix is symmetric positive definite.
    Returns False otherwise.
    For a matrix to be SPD, all eigenvalues must be positive.
    >>> import numpy as np
    >>> matrix = np.array([
    ... [4.12401784, -5.01453636, -0.63865857],
    ... [-5.01453636, 12.33347422, -3.40493586],
    ... [-0.63865857, -3.40493586,  5.78591885]])
    >>> _is_matrix_spd(matrix)
    True
    >>> matrix = np.array([
    ... [0.34634879,  1.96165514,  2.18277744],
    ... [0.74074469, -1.19648894, -1.34223498],
    ... [-0.7687067 ,  0.06018373, -1.16315631]])
    >>> _is_matrix_spd(matrix)
    False
    """
    # Ensure matrix is square.
    assert np.shape(matrix)[0] == np.shape(matrix)[1]

    # If matrix not symmetric, exit right away.
    if np.allclose(matrix, matrix.T) is False:
        return False

    # Get eigenvalues and eignevectors for a symmetric matrix.
    eigen_values, _ = np.linalg.eigh(matrix)

    # / Check sign of all eigenvalues.
    # / np.all returns a value of type np.bool_
    return bool(np.all(eigen_values > 0))
def _create_spd_matrix(dimension: int) -> Any:
    """
    Returns a symmetric positive definite matrix given a dimension.
    Input:
    dimension gives the square matrix dimension.
    Output:
    spd_matrix is an diminesion x dimensions symmetric positive definite (SPD) matrix.
    >>> import numpy as np
    >>> dimension = 3
    >>> spd_matrix = _create_spd_matrix(dimension)
    >>> _is_matrix_spd(spd_matrix)
    True
    """
    random_matrix = np.random.randn(dimension, dimension)
    spd_matrix = np.dot(random_matrix, random_matrix.T)
    assert _is_matrix_spd(spd_matrix)
    return spd_matrix


def conjugate_gradient(
    spd_matrix: np.ndarray,
    load_vector: np.ndarray,
    max_iterations: int = 1000,
    tol: float = 1e-8,
) -> Any:
    """
    Returns solution to the linear system np.dot(spd_matrix, x) = b...