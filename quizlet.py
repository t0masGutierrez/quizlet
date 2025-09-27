import os

base = os.path.expanduser("~") + "/Obsidian/brainTwo/"
output = os.path.expanduser("~") + "/Downloads/Obsidian/"

for dir in os.listdir(base): # loop through folders inside obsidian
    if not dir.startswith(".") and dir not in ["Templates", "Linguistics"]:
        folder_name = dir
        folder_path = base + folder_name

        for file in os.listdir(folder_path): # loop through files inside obsidian folder
            if file.endswith(".md"):
                file_path = folder_path + "/" + file
                file_name = os.path.basename(file)
                file_name = file_name.removesuffix(".md")

                with open(file_path, "r") as md: # read from .md files
                    data = md.read()
                    os.makedirs(output + folder_name + "/", exist_ok=True)

                    with open(output + folder_name + "/" + file_name + ".txt", "w") as txt: # write to .txt files
                        txt.write(data)

                    with open(output + folder_name + "/" + file_name + ".txt", "r") as txt: # read from .txt files
                        lines = txt.readlines()
                        len_lines = len(lines[:-2])

                        for i in range(len_lines): # loop through lines inside .txt file

                            pattern = not lines[i].startswith("- ") and lines[i+1].startswith("- ")
                            pattern1 = lines[i+1].startswith("$$") and not lines[i+2].startswith("---")
                            if pattern or pattern1: # add newlines between term and definition
                                lines[i] += "\n"
                            
                            pattern2 = lines[i].startswith("![[")
                            if pattern2: # remove image embeddings
                                lines[i] = ""
                        
                        with open(output + folder_name + "/" + file_name + ".txt", "w") as txt: # write to .txt files
                            txt.writelines(lines)
