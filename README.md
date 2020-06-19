# Dear Diary

## About
This tool was created to enable pentesters/developers/sysadmins to log what they are doing
during a certain task or  engagement. The output can then be read as diary entries
which can be useful if problems do occur. 

## Getting started
### Setup packages
    pip3 install -r requirements.txt

## Tool Options
### -f File Name
    python3 dear-diary.py -o <path_to_folder> -f ""

### -n Name Entry
    python3 dear-diary.py -o <path_to_folder> -n "Web App"

### -p People Entry
    python3 dear-diary.py -o <path_to_folder> -p "Bob M"

### -i Additional Information Entry
    python3 dear-diary.py -o <path_to_folder> -i "Code 0000"

## Todo
* Add colour syntax codes
* Export notes as html
* Clean up the code 