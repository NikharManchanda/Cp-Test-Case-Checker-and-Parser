import os

import click
import shutil
from pathlib import Path 
import os
from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

template='/home/nm/Code/Sublime/template.cpp'
solpath='/home/nm/Code/Sublime/solution.cpp'
solDir='/home/nm/Code/Sublime/'

def prepend_line(file_name, line):
    """ Insert given string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = file_name + '.cpp'
    # open original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)


@click.command()
def cli():
    click.secho("Template Copied",fg='green') 
    line='/**\n'+' *    author:  Rahkin\n'+f' *    created: {dt_string} \n'+'**/\n'
    myfile = Path(solpath)
    myfile.touch(exist_ok=True)
    f = open(myfile,'w')    
    shutil.copyfile(template,myfile)
    prepend_line(solpath,line)
    f.close()
    os.system("clion "+solpath)    
    pass