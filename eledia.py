import os


def eledia_text(id: int, dir: str) -> str:
    """
    Reads all '.eledia' files within the given directory and its subdirectories,
    collects lines matching the specified ID, and returns a concatenated string
    of their contents sorted by file names within each directory level.
    """
    try:
        file_content_dict = {}

        def recursive_read(root: str, level: int):
            """
            Recursively reads files and directories starting from the root,
            collecting '.eledia' files' content into file_content_dict.
            """
            files = [f for f in os.listdir(root) if os.path.isfile(os.path.join(root, f))]
            
            # Add files to file_content_dict at the current level
            for file in sorted(files):
                if file.endswith('.eledia'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r') as f:
                            for line in f:
                                parts = line.strip().split(':')
                                if len(parts) == 2 and str(id) == parts[0]:
                                    content = parts[1]
                                    if level in file_content_dict:
                                        file_content_dict[level].append((file, content))
                                    else:
                                        file_content_dict[level] = [(file, content)]
                    except Exception as e:
                        print(f'\tCould not read file {file_path}: {e}')
            
            # Recursively traverse subdirectories
            subdirectories = [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))]
            for subdir in subdirectories:
                recursive_read(os.path.join(root, subdir), level + 1)
        
        # Start recursion from the root directory
        recursive_read(dir, 1)
        
        result_as_string = ''
        # Sort according to file name in each level and concatenate their contents
        for level in file_content_dict:
            file_content_dict[level] = sorted(file_content_dict[level], key=lambda x: x[0])
            result_as_string += ' '.join([t[1] for t in file_content_dict[level]])+' '
        
        return result_as_string.strip()
    
    except Exception as e:
        print(f"Error reading directory {dir}: {e}")
        return ""
                

def print_according_to_dir_level (file_content_map):
    for level, files in file_content_map.items():
        print(f"Level {level}:")
        for file, content in files:
            print(f"  File: {file}")
            print(f"  Text:{content}")



if __name__ == "__main__":  
    # Specify the directory you want to scan
    directory_to_scan = os.path.join(os. getcwd(),'test_dir')
    result = eledia_text(1, directory_to_scan)
    print(result)


