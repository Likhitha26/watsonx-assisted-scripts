# Assisted by watsonx Code Assistant 
import sys
import subprocess

def find_macro_commits(repo_path, macro_name):
    command = f"git -C {repo_path} log -S'{macro_name}' --pretty=format:%H"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    commit_hashes = output.decode().strip().split('\n')
    return commit_hashes

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <repo_path> <macro_name>")
        sys.exit(1)

    repo_path = sys.argv[1]
    macro_name = sys.argv[2]

    commit_hashes = find_macro_commits(repo_path, macro_name)

    for commit_hash in commit_hashes:
        print(commit_hash)

