import os

def update_class_in_labels(folder_path, old_class=4, new_class=0):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            updated_lines = []
            with open(file_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split()
                    if parts and int(parts[0]) == old_class:
                        parts[0] = str(new_class)
                    updated_lines.append(" ".join(parts) + "\n")
            with open(file_path, "w") as file:
                file.writelines(updated_lines)
            print(f"Updated: {filename}")

# Example usage
update_class_in_labels("path/to/yolo/labels", old_class=4, new_class=0)