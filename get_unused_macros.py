# Assisted by watsonx Code Assistant 

import os
import sys
import re

def find_unique_macros(directory):
    with open('unused_macros.txt', 'w') as output_file:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.c'):
                    filename = os.path.join(root, file)
                    with open(filename, 'r') as f:
                        content = f.read()

                    # Find multi-line macros
                    macro_pattern = r'^\s*#\s*define\s+(\w+)\s+[^\s#]+\s*(?:\\[^\n]*[^\s#]+)*'
                    macros = re.findall(macro_pattern, content, re.MULTILINE | re.DOTALL)

                    macro_count = {}
                    for macro in macros:
                        macro_count[macro] = len(re.findall(r'\b' + re.escape(macro) + r'\b', content))

                    unique_macros = [macro for macro, count in macro_count.items() if count == 1]

                    if unique_macros:
                        output_file.write(f"Macros in {filename}:\n")
                        for macro in unique_macros:
                            output_file.write(f"{macro}\n")
                        output_file.write("\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python find_unique_macros.py <directory>")
    else:
        find_unique_macros(sys.argv[1])


