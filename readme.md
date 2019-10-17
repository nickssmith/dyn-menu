**CSVs**

Create a csv file in either the "dyn-menu" or "csvs" directories
   
   It can be structured like example.csv
    
    Menu title 1,echo one
    Menu title 2,echo "Any bash can go here"
    menu title 3,echo "even if it needs arguments"
    pass this a dir to run du on, du -h
    any string, echo "try passing this a dir too" && ls

**Making menu scripts**

To prepare to make menus, open the `tmpl` file (its just plaintext) and change the paths to your local directories
 (the ones that say `/home/nick/....`)

To make menu scripts, in `make_menus.py` change the `bin_path` variable to a directory where you want menu scripts to be put
I recommend making a dir and adding it to your path for easy menu calling

**Example file Structure**

This is "Scripts" folder in my home directory

── bin
│   ├── lxc-menu
│   ├── make-menus
│   └── two
├── dyn-menu
│   ├── csvs
│   │   ├── example.csv
│   │   ├── lxc-menu.csv
│   │   └── two.csv
│   ├── csv_tests.py
│   ├── make_menus.py
│   ├── menu.py
│   ├── pip.conf
│   ├── readme
│   ├── test1
│   └── tmpl
├── lxc
│   ├── enter-copy.sh
│   ├── make-lxc.sh
│   ├── rm-lxc.sh
│   ├── set-container-as-local-klaviyo.sh
│   ├── ssh-container.sh
│   ├── start-all-lxc.sh
│   ├── start-container.sh
│   └── stop-all-lxc.sh
├── python
│   ├── ssh_log.csv
│   └── ssh_manage.py
└── venvs
    └── dyn-menu
        ├── bin
        │   ├── activate


**Example Menu**

   example.csv is structured like
    
    Menu title 1,echo one
    Menu title 2,echo "Any bash can go here"
    menu title 3,echo "even if it needs arguments"
    pass this a dir to run du on, du -h
    any string, echo "try passing this a dir too" && ls

  and will show a menu like
    
        example
      
    1. [M]enu title 
    2. M[e]nu title 2
    3. me[n]u title 3
    4. [p]ass this a dir to run du on
    5. [a]ny string
    
**Usage**

For the example menu
        example
      
    1. [M]enu title 
    2. M[e]nu title 2
    3. me[n]u title 3
    4. [p]ass this a dir to run du on
    5. [a]ny string

Pushing the number that corresponds to the menu entry will run that entry

Pushing the letter that is bracketed will also run the corresponding menu entry; 1 or "M" to run the first item in the menu

Arrow keys + Enter key can also be used


   