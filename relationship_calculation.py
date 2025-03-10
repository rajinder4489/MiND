import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

def generate_protein_relationship_equation(protein_a_expression, protein_b_expression):
    """
    Generate an equation for deriving the value of protein B based on the expression of protein A.
    
    :param protein_a_expression: List of expression values for protein A
    :param protein_b_expression: List of expression values for protein B
    :return: A string representation of the equation and the model
    """
    # Reshape the input data
    X = np.array(protein_a_expression).reshape(-1, 1)
    y = np.array(protein_b_expression)

    # Try different polynomial degrees
    best_degree = 1
    best_mse = float('inf')
    best_model = None

    for degree in range(1, 4):  # Try linear, quadratic, and cubic relationships
        poly_features = PolynomialFeatures(degree=degree, include_bias=False)
        X_poly = poly_features.fit_transform(X)

        model = LinearRegression()
        model.fit(X_poly, y)

        y_pred = model.predict(X_poly)
        mse = mean_squared_error(y, y_pred)

        if mse < best_mse:
            best_mse = mse
            best_degree = degree
            best_model = model

    # Generate the equation string
    coefficients = best_model.coef_
    intercept = best_model.intercept_

    equation = f"Protein B = {intercept:.4f}"
    for i, coef in enumerate(coefficients):
        if i == 0:
            equation += f" + {coef:.4f} * Protein A"
        else:
            equation += f" + {coef:.4f} * Protein A^{i+1}"

    # Visualize the relationship
    plt.scatter(X, y, color='blue', label='Actual data')
    X_plot = np.linspace(min(X), max(X), 100).reshape(-1, 1)
    X_poly_plot = PolynomialFeatures(degree=best_degree, include_bias=False).fit_transform(X_plot)
    y_plot = best_model.predict(X_poly_plot)
    plt.plot(X_plot, y_plot, color='red', label='Predicted relationship')
    plt.xlabel('Protein A Expression')
    plt.ylabel('Protein B Expression')
    plt.title('Protein A vs Protein B Expression Relationship')
    plt.legend()
    plt.show()

    return equation, best_model

# Example usage:
# protein_a_values = [1, 2, 3, 4, 5]
# protein_b_values = [2, 4, 5, 4, 6]
# equation, model = generate_protein_relationship_equation(protein_a_values, protein_b_values)
# print(f"Generated equation: {equation}")
