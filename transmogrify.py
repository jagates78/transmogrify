import math
def transmogrify(things, filter_predicate, operation):

    def is_float(x):
        try:
            float(x)
            return True
        except:
            return False

    if filter_predicate == 'float':
        filtered_things = [float(x) for x in things if is_float(x)]
    elif filter_predicate == 'odd':
        filtered_things = [float(x) for x in things if is_float(x) and float(x) % 2 == 1]
    elif filter_predicate == 'even':
        filtered_things = [float(x) for x in things if is_float(x) and float(x) % 2 == 0]
    else:
        raise ValueError(f'Unknown filter predicate: {filter_predicate}')

    if operation == 'sum':
        result = sum(filtered_things)
    elif operation == 'multiply':
        result = math.prod(filtered_things) if filtered_things else 0
    else:
        raise ValueError(f'Unknown operation: {operation}')

    return result
