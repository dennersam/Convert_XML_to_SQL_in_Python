import PySimpleGUI as sg
import Converter

if __name__ == '__main__':
    layout = [[sg.Text('Selecione o arquivo XML')],
               [sg.Input(), sg.FileBrowse()],
               [sg.Submit('Converter'), sg.Cancel('Cancelar')]]

    window = sg.Window('Converter XML para SQL', layout)
    event, values = window.read()