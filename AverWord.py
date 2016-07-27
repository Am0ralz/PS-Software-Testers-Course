# http://tkinter.unpythonic.net/wiki/tkFileDialog
# http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
# http://www.tkdocs.com/tutorial/windows.html#dialogs
import tkinter
from tkinter import filedialog
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()
cont = True
options = {'defaultextension': '.txt', 'filetypes': [('text files', '.txt')], 'parent': root}

result = messagebox.askyesno(type='yesno',
                             message='Welcome! Would you like to use Control Your Type? We only accept text files (.txt)',
                             icon='question',
                             title='Control Your Type')

while cont:
    numword = 0
    numsent = 0
    if result:
        filename = filedialog.askopenfilename(**options)
        with open(filename, 'r') as f:
            for line in f:
                for word in line.split():
                    if (word[-1] == '.' or word[-1] == '!' or word[-1] == ',' or word[-1] == ';' or word[-1] == ':' or
                                word[-1] == '?'):
                        numsent += 1
                    if len(word) >= 3:
                        numword += 1

            average = numword / numsent
            aver = str(average)
            text = "Your average word count is " + aver
            messagebox.showinfo(message=text)
            cont = messagebox.askyesno(type='yesno',
                                       message='Hello again, Do you want to use Control Your Type again with other text files? ',
                                       icon='question',
                                       title='Continue')
    else:
        cont = False
