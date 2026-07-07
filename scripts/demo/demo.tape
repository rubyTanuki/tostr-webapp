Output ../../public/demo.webm

# Configure the UI to match your Vite/Figma design
Set Theme { "background": "#1C1E22", "foreground": "#cdd6f4", "cursor": "#f5e0dc" }
Set Width 900
Set Height 600
Set Padding 0
Set FontSize 22
Set Framerate 60
Set CursorBlink true

# ---------------------------------------------------
# SETUP: Hide the setup commands from the viewer
# ---------------------------------------------------
Hide
Type 'alias tostr="python3 demo_search.py"'
Enter
Type 'clear'
Enter
Show

# ---------------------------------------------------
# SCENE 1: The Semantic Search
# ---------------------------------------------------
Sleep 1s
Type 'tostr search "authentication" --filter class --top-k 3'
Sleep 500ms
Enter

# Leave the search results on screen for 3 seconds
Sleep 2.5s

# Make it look like the user is clearing the terminal for the next command
Type "clear"
Sleep 500ms
Enter

# ---------------------------------------------------
# TRANSITION: Swap the alias silently
# ---------------------------------------------------
Hide
Type 'alias tostr="python3 demo_inspect.py"'
Enter
Type 'clear'
Enter
Show

# ---------------------------------------------------
# SCENE 2: The Deep Dive Inspect
# ---------------------------------------------------
Type "tostr inspect 'C-a1b2c3d4e5' ."
Sleep 500ms
Enter

# Leave the inspect results on screen for 4 seconds before looping
Sleep 2.5s

# Make it look like the user is clearing the terminal for the next command
Type "clear"
Sleep 500ms
Enter
Sleep 500ms