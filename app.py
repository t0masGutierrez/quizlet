import streamlit as st
from quizlet import md_to_txt

def home():
    st.session_state.clear()
    show_folders()

def show_folders():
    """
    Show all of the folders as clickable buttons
    """
    obsidian = md_to_txt()
    folders = []
    for vault in obsidian:
        if vault not in st.session_state:
            folders.append(vault)
            st.session_state[vault] = False

    def hide_folders(dir, obsidian=obsidian):
        """
        Hide all of the folders

        Parameters
        ----------
        dir : string
            Name of clicked directory

        Returns
        -------
        dir : string
            Name of clicked directory
        """
        for f in folders:
            st.session_state[f] = False
        show_files(dir)
    
    for f in folders:
        if not st.session_state[f]:
            st.button(f, width="stretch", on_click=hide_folders, args=[f])

def show_files(dir):
    """
    Show all of the files of folder as clickable buttons

    Parameters
    ----------
    dir : string
            Name of clicked directory
    """
    st.button("Back", on_click=home)
    obsidian = md_to_txt()
    file_names = []
    file_paths = []
    for vault, subvault in obsidian.items():
        if vault == dir:
            for file_name in subvault:
                file_names.append(file_name)
                file_paths.append(subvault[file_name])
                if file_name not in st.session_state:
                    st.session_state[file_name] = False

    def hide_files(index, subdir, dir=dir):
        """
        Hide all of the files

        Parameters
        ----------
        index : int
            Index of clicked subdirectory

        subdir : string
            Name of clicked subdirectory

        dir : string
            Name of clicked directory

        Returns
        -------
        subdir : string
            Name of clicked subdirectory
        
        file_path : string
            Location of clicked subdirectory
        """
        for f in file_names:
            st.session_state[f] = False
        file_path = file_paths[index]
        show_data(file_path, subdir, dir)

    for i, f in enumerate(file_names):
        if not st.session_state[f]:
            st.button(f, width="stretch", on_click=hide_files, args=[i, f])

def show_data(file_path, subdir, dir):
    """
    Show all of the file data on webpage as markdown

    Parameters
    ----------
    subdir : string
            Name of file
    
    Returns
    -------
    file : string
            Name of subdirectory
    """
    st.title(subdir)
    left, middle, right = st.columns(3)
    folders = left.button("Home", width="stretch", on_click=home)
    files = middle.button(dir, width="stretch", on_click=show_files, args=[dir])
    settings = right.button("Settings", width="stretch")

    with open(file_path, "r") as file:
        data = file.read()
    st.markdown(data)

def main():
    show_folders()

if __name__ == "__main__":
    main()
