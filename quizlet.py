import os

def format():
    """
    Format markdown files
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

                    # read from obsidian files
                    with open(file_path, "r") as obs:
                        data = obs.read()
                        os.makedirs(output + folder_name + "/", exist_ok=True)

                        # write to github files
                        with open(output + folder_name + "/" + file_name + ".md", "w") as git:
                            git.write(data)

                        # read from github files
                        with open(output + folder_name + "/" + file_name + ".md", "r") as git:
                            lines = git.readlines()

                            # loop through lines inside github file
                            for i in range(len(lines)-1):
                                pattern = not lines[i].startswith("- ") and lines[i+1].startswith("- ") 
                                pattern1 = lines[i+1].startswith("$$") and not lines[i+2].startswith("---")
                                pattern2 = lines[i].startswith("$$") and lines[i+1].startswith("---") 
                                pattern3 = lines[i].startswith("\\")

                                # add hashtags before terms
                                if pattern or pattern1:
                                    lines[i] = "### " + lines[i]
                                    lines[i+1]

                                # add newlines between terms
                                if pattern1 or pattern2:
                                    lines[i] += "\n"
                                
                                # replace alignment
                                if pattern3:
                                    lines[i] = lines[i].replace("align*", "aligned")
                            
                            # write to github files
                            with open(output + folder_name + "/" + file_name + ".md", "w") as git:
                                git.writelines(lines)

def main():
    format()

if __name__ == "__main__":
    main()