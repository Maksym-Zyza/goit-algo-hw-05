import timeit
import os
from boyer_moore import boyer_moore
from kmp import kmp
from rabin_karp import rabin_karp


def read_file(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} not found")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            if not content:
                raise ValueError(f"File {file_path} is empty")
            return content
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


def compare_algorithms(file_paths, existing_pattern, non_existing_pattern):
    algorithms = {"Boyer-Moore": boyer_moore, "KMP": kmp, "Rabin-Karp": rabin_karp}
    number = 100

    for file_path in file_paths:
        print(f"\nProcessing {file_path}:")
        text = read_file(file_path)
        if text is None:
            continue

        for pattern_name, pattern in [
            ("Existing", existing_pattern),
            ("Non-existing", non_existing_pattern),
        ]:
            if not pattern:
                print(f"Skipping {pattern_name} pattern: empty pattern")
                continue
            print(f"\n{pattern_name} pattern ('{pattern}'):")
            for algo_name, algo_func in algorithms.items():
                try:
                    stmt = f"algo_func(text, pattern)"
                    time = timeit.timeit(
                        stmt,
                        number=number,
                        globals={
                            "algo_func": algo_func,
                            "text": text,
                            "pattern": pattern,
                        },
                    )
                    print(f"{algo_name}: {time:.6f} seconds")
                except Exception as e:
                    print(f"Error in {algo_name}: {e}")


if __name__ == "__main__":
    file_paths = ["article_1.txt", "article_2.txt"]
    existing_pattern = "інтервал sqrt"
    non_existing_pattern = "nonexistent123"
    compare_algorithms(file_paths, existing_pattern, non_existing_pattern)