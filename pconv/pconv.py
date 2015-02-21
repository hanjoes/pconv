#!/usr/bin/python3.4

__author__ = 'hanjoes'


import sys
import tkinter
import cchardet
import codecs

from tkinter import filedialog


""" this class is for text file conversions. """
class conv:
    def __init__(self):
        pass

    """ set input file """
    def set_input(self, path, encoding='unicode'):
        self.input_path = path
        self.input_encoding = encoding

    def set_output(self, path, encoding='unicode'):
        self.output_path = path
        self.output_encoding = encoding

    def convert(self):
        try:
            output_file = open(self.output_path, 'w+', 1)
            with codecs.open(self.input_path, 'r', self.input_encoding) as f:
                for line in f:
                    encoded_line = codecs.encode(line, self.output_encoding)
                    output_file.write(line)
            return True
        except ValueError:
            print('decode failed due to incorrect character encoding')
            return False

class ConvGUI():
    def __init__(self):
        super().__init__()

        self.top_window = tkinter.Tk()
        self.top_window.title('Text to UTF-8 Converter')
        # add frame
        self.frame = tkinter.Frame(self.top_window)
        self.frame.pack(expand=1)

        # add button
        self.input_selection_button = tkinter.Button(self.frame, text='Input', command=self.choose_input)
        self.input_selection_button.grid(column=1, row=3, sticky='W')
        self.output_selection_button = tkinter.Button(self.frame, text='Output', command=self.choose_output)
        self.output_selection_button.grid(column=7, row=3, sticky='W')
        self.convert_button = tkinter.Button(self.frame, text='Convert', command=self.convert)
        self.convert_button.grid(column=4, row=4)

        # display filename labels
        self.input_filename_label = tkinter.Label(self.frame, text='No Input')
        self.input_filename_label.grid(column=1, row=2, sticky='W')
        self.output_filename_label = tkinter.Label(self.frame, text='No Output')
        self.output_filename_label.grid(column=7, row=2, sticky='W')
        self.output_status_label = tkinter.Label(self.frame, text='Click Input')
        self.output_status_label.grid(column=4, row=3, sticky='W')


    def start(self):
        self.center_window()
        self.run()

    def center_window(self):
        w = 300
        h = 150

        sw = self.frame.winfo_screenwidth()
        sh = self.frame.winfo_screenheight()

        x = sw / 2
        y = sh / 2

        self.top_window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def run(self):
        self.top_window.mainloop()

    def choose_input(self):
        self.input_filename = filedialog.askopenfilename(parent=self.top_window)
        if self.input_filename != None:
            rawdata = open(self.input_filename,'rb').read()
            encoding = cchardet.detect(rawdata)['encoding']
            self.input_filename_label['text'] = encoding
            self.input_file_encoding = encoding

    def choose_output(self):
        self.output_filename = self.output_filename = filedialog.asksaveasfilename(parent=self.top_window)
        if self.output_filename != None:
            l = str(self.output_filename).split('/')
            self.output_filename_label['text'] = l[len(l)-1]

    def convert(self):
        c = conv()

        c.set_input(self.input_filename, self.input_file_encoding)
        c.set_output(self.output_filename, 'UTF-8')

        if c.convert():
            self.output_status_label['foreground'] = 'sea green'
            self.output_status_label['text'] = 'Succeeded'
        else:
            self.output_status_label['foreground'] = 'red'
            self.output_status_label['text'] = 'Failed'

def main(argv):
    window_gui = ConvGUI()
    window_gui.start()

if __name__ == '__main__':
    main(sys.argv)



