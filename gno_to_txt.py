import os

# Path to the cloned repository directory
repo_path = '/home/muss/gno'
# Base path for the output files
output_file_base = '/home/muss/automatisation/txt'

# Maximum file size in bytes (20 MB)
max_file_size = 2 * 1024 * 1024

# File extensions to extract
extensions = ['.gno', '.md', '.json', '.txt', '.go' , '.sh', '.yml', '.yaml', '.mod', '.sum', '.gitignore', '.gitattributes', '.dockerignore', '.Dockerfile', '.dockerfile', '.env', '.env.example', '.env.sample', '.env.test', '.env.local', '.env.development', '.env.production', '.env.staging', '.env.ci', '.env.netlify', '.env.vercel', '.env.local.example', '.env.development.example', '.env.production.example', '.env.staging.example', '.env.ci.example', '.env.netlify.example', '.env.vercel.example', '.env.local.sample', '.env.development.sample', '.env.production.sample', '.env.staging.sample', '.env.ci.sample', '.env.netlify.sample', '.env.vercel.sample', '.env.local.test', '.env.development.test', '.env.production.test', '.env.staging.test', '.env.ci.test', '.env.netlify.test', '.env.vercel.test',]

file_index = 1
current_file_path = f"{output_file_base}_{file_index}.txt"
current_file_size = 0

# Open the first output file in write mode
output_file = open(current_file_path, 'w')

# Traverse the repository and read the selected files
for root, dirs, files in os.walk(repo_path):
    for file in files:
        if any(file.endswith(ext) for ext in extensions):
            full_path = os.path.join(root, file)
            
            # Write the file name as a title (optional)
            title = f"\n\n===== {full_path} =====\n\n"
            content = ""
            
            # Read the file content
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Calculate the total size of the content to write
            total_content_size = len(title.encode('utf-8')) + len(content.encode('utf-8'))
            
            # If adding this content exceeds the max size, close the current file and open a new one
            if current_file_size + total_content_size > max_file_size:
                output_file.close()
                file_index += 1
                current_file_path = f"{output_file_base}_{file_index}.txt"
                output_file = open(current_file_path, 'w')
                current_file_size = 0
            
            # Write the title and content to the file
            output_file.write(title)
            output_file.write(content)
            current_file_size += total_content_size

# Close the last output file
output_file.close()

print("Concatenation completed and files split!")
