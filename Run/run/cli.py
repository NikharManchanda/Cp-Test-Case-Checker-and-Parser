from sys import stderr
import click
import json
from pathlib import Path 
import os
import subprocess

template='/home/nm/Code/Sublime/template.cpp'
solpath='/home/nm/Code/Sublime/solution.cpp'
solDir='/home/nm/Code/Sublime/'

def changeDir():
    global solDir
    os.chdir('..')
    os.chdir(solDir)

def compile():
    compilecmd='g++ -std=c++17 -Wshadow -Wall -o solution -O2 -Wno-unused-result'
    listcompile=compilecmd.split(' ')
    listcompile.append('solution.cpp')
    x=subprocess.call(listcompile)
    return x
def run():
    os.system('./solution')

def build():
    compilecmd='g++ -std=c++11 -O0 -Wall -Wextra -Wno-unused-result -Wno-char-subscripts -Wshadow -Wfloat-equal -Wconversion -Wformat-signedness -Wvla -Wduplicated-cond -Wlogical-op -Wredundant-decls -ggdb3 -D_GLIBCXX_DEBUG -D_GLIBCXX_DEBUG_PEDANTIC -D_FORTIFY_SOURCE=2 -fsanitize=undefined,address,float-divide-by-zero,float-cast-overflow -fno-omit-frame-pointer -fno-optimize-sibling-calls -fstack-protector-all -fno-sanitize-recover=all -o solution'
    listcompile=compilecmd.split(' ')
    listcompile.append('solution.cpp')
    x=subprocess.call(listcompile)
    return x

@click.command()
def cli():
    changeDir()
    global solDir,solpath  
    f2 = open(solDir+"tests", "r")  
    lines=f2.readlines()[0]
    f2.close()
    cases=json.loads(lines)
    correct=0
    testCase=0
    returnstatus=compile()
    if returnstatus != 0:
        click.secho('Compilation Error',fg='bright_red')
        return
    for case in cases:
        testCase+=1
        ans=case['correct_answers']
        input=case['test']
        if isinstance(ans, list):
            ans=ans[0].strip()
        else:
            ans=ans.strip()
        if isinstance(input, list):
            input=input[0].strip()
        else:
            input=input.strip()
        myfile = Path(solDir+'input.txt')
        myfile.touch(exist_ok=True)
        f = open(myfile,'w')    
        f.writelines(input)
        f.close()
        
        # run()


        # with open(solDir+'/'+"output.txt", 'r') as file:
        #     myanswers = file.read().strip()
        subpro = subprocess.Popen("./solution", shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        myanswers = subpro.stdout.read().decode('UTF-8').strip()
        click.secho(f'Test Case {testCase} :',fg='cyan')
        click.secho("Input:",fg='bright_magenta')
        click.echo(input)
        click.secho('Your Answer:',fg='bright_magenta')
        run()
        click.secho('\nExpected Answer:',fg='bright_magenta')
        click.echo(ans)

        if (myanswers==ans):
            correct+=1
            click.secho(f'Passed ✅\n',fg='green')
        else:
            click.secho(f'Failed ❌\n',fg='red')
        
            
    if testCase==correct:
        click.secho('✅ Correct Answer ✅',fg='bright_green')
    else:
        click.secho(f'❌ Wrong Answer --> {correct}/{testCase} Cases Passed',fg='bright_red')


