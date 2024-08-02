import whois
from itertools import permutations
import time
import concurrent.futures

# List of domain keywords and TLDs
domain_keywords = [
    "vector", "labs", "lambda", "binary", "fractal", "quantum", "topology",
    "matrix", "proxy", "bit", "logic", "carbon", "silicon"
]

# Filter out any keywords that start with "labs" for the first position
first_position_keywords = [word for word in domain_keywords if not word.startswith("labs")]
second_position_keywords = domain_keywords

tlds = [
    ".com",
    ".io",
    ".net"
]

def generate_combinations(keywords1, keywords2, max_length):
    combinations_set = set()
    for r in range(1, 3):  # Limit to combinations of 1 or 2 keywords
        for combo in permutations(keywords1, r):
            joined_combo = ''.join(combo)
            if len(joined_combo) <= max_length:
                combinations_set.add(joined_combo)
        if r == 2:
            for word1 in keywords1:
                for word2 in keywords2:
                    if word1 != word2:
                        joined_combo = word1 + word2
                        if len(joined_combo) <= max_length:
                            combinations_set.add(joined_combo)
    return combinations_set

def check_domain_availability(domain):
    try:
        w = whois.whois(domain)
        if w.status is None:
            return f"{domain} is available"
        else:
            return f"{domain} is taken"
    except whois.parser.PywhoisError:
        return f"{domain} is available"
    except Exception as e:
        return f"Unexpected error for {domain}: {e}"

# Generate combinations with a length limit of 15 characters
max_length = 15
domain_combinations = generate_combinations(first_position_keywords, second_position_keywords, max_length)
print(f"Generated {len(domain_combinations)} combinations")  # Debug print

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for domain_name in domain_combinations:
            for tld in tlds:
                domain = domain_name + tld
                futures.append(executor.submit(check_domain_availability, domain))

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if "available" in result:
                print(result)

if __name__ == "__main__":
    main()
