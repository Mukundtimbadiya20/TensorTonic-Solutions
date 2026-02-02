import math

def winsorize(values, lower_pct, upper_pct):
    # Convert to float (do not modify original list)
    values = [float(v) for v in values]
    n = len(values)

    # Sort a copy for percentile computation
    sorted_vals = sorted(values)

    def percentile_value(pct):
        # k = (n - 1) * p / 100
        k = (n - 1) * pct / 100.0
        lo = int(math.floor(k))
        hi = int(math.ceil(k))

        # Linear interpolation
        if lo == hi:
            return sorted_vals[lo]
        return sorted_vals[lo] + (k - lo) * (sorted_vals[hi] - sorted_vals[lo])

    # Compute bounds
    lower_bound = percentile_value(lower_pct)
    upper_bound = percentile_value(upper_pct)

    # Clip values while preserving order
    result = []
    for v in values:
        if v < lower_bound:
            result.append(lower_bound)
        elif v > upper_bound:
            result.append(upper_bound)
        else:
            result.append(v)

    return result
