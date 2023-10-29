def format_table(benchmarks, algos, results):
    max_benchmark_len = max(len(b) for b in benchmarks)
    header = f"| Benchmark{' ' * (max_benchmark_len - 9)} | quick sort | merge sort | bubble sort |\n\
|{'-' * (max_benchmark_len + 2)}|------------|------------|-------------|"

    print(header)

    for i in range(len(benchmarks)):
        benchmark = benchmarks[i]
        row = f"| {benchmark}{' ' * (max_benchmark_len - len(benchmark))} | {results[i][0]:<10} | {results[i][1]:<10} | {results[i][2]:<11} |"
        print(row)

format_table(["best case", "worst case", "average cases"],
             ["quick sort", "merge sort", "bubble sort"],
             [[1.23, 1.56, 2.0], [3.3, 2.966, 3.9], [2.0, 2.1, 2.2]])
