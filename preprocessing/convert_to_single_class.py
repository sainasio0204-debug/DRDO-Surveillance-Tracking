import os


folder_path = '/path/to/your/labels/folder'

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        
        # Read and modify lines
        with open(file_path, 'r') as f:
            lines = f.readlines()

        # Change the first element (class ID) to '0'
        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if parts:
                parts[0] = '0'
            new_lines.append(' '.join(parts) + '\n')

        # Write back the modified lines
        with open(file_path, 'w') as f:
            f.writelines(new_lines)

print("Class IDs in all files updated to 0.")