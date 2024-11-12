import os
import time
import pandas as pd
from methods import load_methods  # Assuming methods can be dynamically loaded

# Define metrics and results storage
results = []


def benchmark_method(method, dataset):
    """
    Benchmarks a compression method by measuring its compression ratio and times.

    Args:
        method: An object with 'compress' and 'decompress' methods for performing
                compression and decompression operations.
        dataset: The path to the dataset file to be compressed.

    Returns:
        A tuple containing:
        - compression_ratio: The ratio of the original dataset size to the compressed size.
        - compression_time: The time taken to compress the dataset.
        - decompression_time: The time taken to decompress the dataset.
    """
    start_time = time.time()
    compressed_data = method.compress(dataset)
    compression_time = time.time() - start_time

    # Measure compression ratio
    original_size = os.path.getsize(dataset)
    compressed_size = len(compressed_data)
    compression_ratio = original_size / compressed_size

    # Decompression
    start_time = time.time()
    method.decompress(compressed_data)
    decompression_time = time.time() - start_time

    return compression_ratio, compression_time, decompression_time


# Loop through each method and dataset
for method_name, method in load_methods().items():
    for dataset in os.listdir("/app/datasets"):
        ratio, comp_time, decomp_time = benchmark_method(
            method, f"/app/datasets/{dataset}")
        results.append({
            "method": method_name,
            "dataset": dataset,
            "compression_ratio": ratio,
            "compression_time": comp_time,
            "decompression_time": decomp_time
        })

# Save results
df = pd.DataFrame(results)
df.to_csv("/app/results/benchmark_results.csv", index=False)
