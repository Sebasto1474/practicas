def square_root_bisection(square_target, tolerance=0.01, maximum=100):
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if square_target == 0:
        print(f"The square root of {square_target} is {square_target}")
        return square_target
    if square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target
    low = 0
    if square_target < 1:
        high = 1
    else:
        high = square_target
    iterations = 0
    while iterations < maximum:
        mid = (low + high) / 2
        mid_squared = mid * mid
        if mid_squared > square_target:
            high = mid
        if mid_squared < square_target:
            low = mid
        iterations += 1
        if (high - low) <= tolerance:
            mid = (low + high) / 2
            print(f"The square root of {square_target} is approximately {mid}")
            return mid
    print(f"Failed to converge within {iterations} iterations")
    return None