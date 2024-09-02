# Game Compiler Manager


## Purpose of the Project

The purpose of the GameCompilerManager project is to streamline the management, compilation, and organization of game development directories. It automates repetitive tasks that game developers often encounter, such as discovering game directories, compiling game code, and generating metadata files, thus making the development process more efficient and organized.


## Features
- Automatic Directory Search: Quickly finds all your game directories based on a specified pattern.
- Code Compilation: Compiles your game code files with just one command.
- Easy Directory Management: Effortlessly copies and organizes your game directories.
- Metadata Generation: Creates a handy JSON file with details about your game directories.

<br />
<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>ChatGPT</b>
- <b>Powershell</b>

<h2>Environments Used </h2>

- <b>Visual Studio Code </b>

## Script Breakdown

   - find_all_game_paths(source): Searches for all directories containing game code based on a pattern.
   - get_name_from_paths(paths, to_strip): Strips a specified pattern from directory names and returns the modified names.
   - create_dir(path): Creates a directory if it does not already exist.
   - copy_and_overwrite(source, dest): Copies the source directory to the destination, overwriting if necessary.
   - make_json_metadata_file(path, game_dirs): Generates a JSON file with metadata about the game directories.
   - compile_game_code(path): Compiles game code files within the specified directory.
   - run_command(command, path): Executes a command in the given path and prints the result.
  
