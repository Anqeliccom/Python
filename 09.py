def format_table(benchmarks, algos, results):
    num_benchmarks = len(benchmarks)
    num_algos = len(algos)
    
    max_benchmark_len = max(len(b) for b in benchmarks)
    max_result_lens = [max(len(str(results[i][j])) for i in range(num_benchmarks)) for j in range(num_algos)]
    
    max_space_between_algos_results = [max(max_result_lens[i], len(algo)) for i, algo in enumerate(algos)]


    header = f"| Benchmark{' ' * (max_benchmark_len - 9)} |"
    for algo, max_len in zip(algos, max_space_between_algos_results):
        header += f" {algo}{' ' * (max_len - len(algo))} |"
    print(header)
    
    header_line = f"|{'-' * (max_benchmark_len + 2)}|"
    for max_len in max_space_between_algos_results:
        header_line += f"{'-' * (max_len + 2)}|"
    print(header_line)
    
    for i in range(num_benchmarks):
        benchmark = benchmarks[i]
        row = f"| {benchmark}{' ' * (max_benchmark_len - len(benchmark))} |"
        for j in range(num_algos):
            row += f" {results[i][j]}{' ' * (max_space_between_algos_results[j] - len(str(results[i][j])))} |"
        print(row)

format_table(["best case", "worst cases", "average cases"],
             ["quick sort", "merge sort", "bubble sorted"],
             [[1.23, 1.56, 2.0], [3.3, 2.966, 3.9], [2.0, 2.1, 2.2]])
