#!/bin/bash

# Function to copy folder "x" to a target directory
copy_folder() {
    local target_dir=$1
    if [ -d "$target_dir" ]; then
        cp -r evaluation_world "$target_dir"
        echo "Folder 'evaluation_world' has been copied to '$target_dir'."
    else
        echo "Target directory '$target_dir' does not exist. Creating it now."
        mkdir -p "$target_dir"
        cp -r evaluation_world "$target_dir"
        echo "Folder 'evaluation_world' has been copied to '$target_dir'."
    fi
}

# Determine the OS and set the Minecraft saves directory
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    minecraft_dir="$HOME/.minecraft/saves"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    minecraft_dir="$HOME/Library/Application Support/minecraft/saves"
elif [[ "$OSTYPE" == "cygwin" ]]; then
    minecraft_dir="$(cygpath -u "$APPDATA")/.minecraft/saves"
elif [[ "$OSTYPE" == "msys" ]]; then
    minecraft_dir="$APPDATA/.minecraft/saves"
elif [[ "$OSTYPE" == "win32" ]]; then
    minecraft_dir="$APPDATA/.minecraft/saves"
else
    echo "Unsupported OS: $OSTYPE"
    exit 1
fi

# Call the function to copy the folder
copy_folder "$minecraft_dir"