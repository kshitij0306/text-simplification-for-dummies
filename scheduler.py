import random
import logging


def get_weights(i, n):
    weights_by_step = {
        0: [0.7, 0.2, 0.1],
        n // 3: [0.1, 0.7, 0.2],
        2 * n // 3: [0.2, 0.1, 0.7],
    }

    if i < 0:
        raise ValueError("i must be non-negative")
    if i > 0 and i < n // 3:
        return weights_by_step[0]
    elif i >= n // 3 and i < 2 * n // 3:
        return weights_by_step[n // 3]
    else:
        return weights_by_step[2 * n // 3]


def choose_number(n=100):
    # Let's initialize initial weights based on the number of batches in each loader
    choices = []
    for i in range(n):
        # Choose a number based on weights
        weights = get_weights(i, n)
        chosen_number = random.choices([1, 2, 3], weights)[0]
        choices.append(chosen_number)
        yield chosen_number

        # Adjust weights over time
        weights[0] *= 0.95  # Decrease weight for 1
        weights[1] *= 1.05  # Increase weight for 2
        weights[2] += 0.005  # Increase weight for 3

        # Normalize weights to ensure they sum to 1
        total_weight = sum(weights)
        weights = [weight / total_weight for weight in weights]

    logging.info(f"Choices: {choices}")
    return choices


def get_batches(l1_loader, l2_loader, l3_loader):
    loaders = {
        1: iter(l1_loader),
        2: iter(l2_loader),
        3: iter(l3_loader)
    }

    finished = {
        1: False,
        2: False,
        3: False
    }

    n = len(l1_loader) + len(l2_loader) + len(l3_loader)
    choices = []
    for choice in choose_number(n):
        # Use the iterator explicitly to get the next batch
        returned = False
        while not returned:
            try:
                p = next(loaders[choice])
                print(f"Selected {choice} difficulty level")
                print(f"Batch: {p[:5]}")
                returned = True
                yield p
            except StopIteration:
                finished[choice] = True
                # Chose a random number from the remaining iterators
                choice = random.choice(list(loaders.keys()))
                # If all iterators are exhausted, stop
            finally:
                choices.append(choice)

        if all(finished.values()):
            break

    logging.info(f"Choices: {choices}")
