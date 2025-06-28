from rich.console import Console
from rich.text import Text
from rich.align import Align

console = Console()

art = [
    "                                                                           ",
    "                                                                           ",
    "                          :%#                                              ",
    "                           *%%#                                            ",
    "                             %%%+            =**+    ***                  ",
    "                              #%%%.        .***.                           ",
    "                                #%%%      ***=                             ",
    ".=========-      .===- =====-    =%%%#  +***      :====-      -:         -.",
    ".+++++++++**     .++****+++**=     #%%%%**=       :++***      **:       +*=",
    "          **.       .*+    =*-      -%%%%.            **       **      :** ",
    "   .-=+*****.       .*+            +**%%%%#           **       :**    .**  ",
    "=***+=-.  **.       .*+            +***#%%#           **        =*+   +*-  ",
    "+*:       **.       .*+             -****.            **         **: +*=   ",
    "+*=.......**.     ..=**....        +%%%****:       ...-**-...      **=**    ",
    ":***********.    +********+      =%%%*  +***.    .**********.     :***     ",
    "                               .%%%#      ***+                             ",
    "        The arXiv             #%%%          ***=                           ",
    "    CLI SEARCH ENGINE       .%%%-            -***                          ",
    "                             ==                =**=                        ",
    "                                                 +*:                       ",
    "                                                                           ",
    "      Thank you to arXiv for use of its open access interoperability.      ",
    "         This project is not endorsed by arXiv or its associates.          "
]

# x_positions is no longer needed for coloring based on the new requirements

def display_logo():
    for line in art:
        output_text = Text("")
        for char in line:
            if char == '%' or char == '#':
                output_text.append(char, style="red")
            elif char != " ":
                output_text.append(char, style="white")
            else:
                output_text.append(" ")
        console.print(output_text) # Removed Align.center
    console.print("\n")