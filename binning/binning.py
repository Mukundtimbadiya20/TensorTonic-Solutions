import math

def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    if len(values) == 0:
        return []

    min_val = min(values)
    max_val = max(values)

    # All values same
    if min_val == max_val:
        return [0] * len(values)

    bin_width = (max_val - min_val) / num_bins

    bin_indices = []
    for x_i in values:
        raw_bin_index = int((x_i - min_val) / bin_width)
        bin_index = min(raw_bin_index, num_bins - 1)
        bin_indices.append(bin_index)

    return bin_indices
