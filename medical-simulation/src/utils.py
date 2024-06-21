import numpy as np

def weighted_choice(choices):
    choices, weights = zip(*choices)
    total = sum(weights)
    probabilities = [weight / total for weight in weights]
    return np.random.choice(choices, p=probabilities)
