#compile a tex file into latex
import subprocess
import shlex

def main(filename):
    subprocess.Popen(shlex.split('pdflatex ' + filename + '.tex'))
    subprocess.call(shlex.split('rm ' + filename + '.log'))
    subprocess.call(shlex.split('rm ' + filename + '.aux'))

if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    if filename[-4:] == '.tex':
        filename = filename[0:-4]
    main(filename)

