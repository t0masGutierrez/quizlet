import os


def md_to_txt(input, output):
    # loop through folders inside obsidian
    for dir in os.listdir(input):
        ignore = ["Templates", "Linguistics"]
        if not dir.startswith(".") and dir not in ignore:
            folder_name = dir
            folder_path = input + folder_name

            # loop through files inside obsidian folder
            for file in os.listdir(folder_path):
                if file.endswith(".md"):
                    file_path = folder_path + "/" + file
                    file_name = os.path.basename(file)
                    file_name = file_name.removesuffix(".md")

                    # read from .md files
                    with open(file_path, "r") as md:
                        data = md.read()
                        os.makedirs(output + folder_name + "/", exist_ok=True)

                        # write to .txt files
                        with open(output + folder_name + "/" + file_name + ".txt", "w") as txt:
                            txt.write(data)

                        # read from .txt files
                        with open(output + folder_name + "/" + file_name + ".txt", "r") as txt:
                            lines = txt.readlines()
                            len_lines = len(lines[:-2])

                            # loop through lines inside .txt file
                            for i in range(len_lines):
                                pattern = not lines[i].startswith("- ") and lines[i+1].startswith("- ")
                                pattern1 = lines[i+1].startswith("$$") and not lines[i+2].startswith("---")

                                # add newlines between term and definition
                                if pattern or pattern1:
                                    lines[i] += "\n"
                            
                            with open(output + folder_name + "/" + file_name + ".txt", "w") as txt: # write to .txt files
                                txt.writelines(lines)
    return None

def main():
    x = os.path.expanduser("~") + "/Obsidian/brainTwo/"
    y = os.path.expanduser("~") + "/Downloads/Obsidian/"
    md_to_txt(x, y)

main()