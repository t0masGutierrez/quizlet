import os

def md_to_txt():
    """
    Convert markdown files to text files
    """
    input = os.path.expanduser("~") + "/Obsidian/brainTwo/"
    output = os.path.expanduser("~") + "/Github/quizlet/obsidian/"
    dirs = {}
    # loop through folders inside obsidian
    for dir in os.listdir(input):
        ignore = ["Templates", "Linguistics", "Brain.base"]
        if not dir.startswith(".") and dir not in ignore:
            folder_name = dir
            folder_path = input + folder_name
            dirs[folder_name] = {}

            # loop through files inside obsidian folder
            for file in os.listdir(folder_path):
                if file.endswith(".md"):
                    file_path = folder_path + "/" + file
                    file_name = os.path.basename(file)[:-3] # remove suffix ".md"
                    dirs[folder_name][file_name] = file_path

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

                            # loop through lines inside .txt file
                            for i in range(len(lines)-2):
                                pattern = not lines[i].startswith("- ") and lines[i+1].startswith("- ")
                                pattern1 = lines[i+1].startswith("$$") and not lines[i+2].startswith("---")

                                # add newlines between term and definition
                                if pattern or pattern1:
                                    lines[i] += "\n"
                            
                            # write to .txt files
                            with open(output + folder_name + "/" + file_name + ".txt", "w") as txt:
                                txt.writelines(lines)

def main():
    md_to_txt()

if __name__ == "__main__":
    main()