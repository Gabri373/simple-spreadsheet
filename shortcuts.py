import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtGui import QColor
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtGui import QFont

app = QApplication(sys.argv)

ui_file = QFile("shortcuts.ui")
ui_file.open(QFile.ReadOnly)
loader = QUiLoader()
window = loader.load(ui_file)
ui_file.close()

# Start
window.showMaximized()

# Settaggio File
MAX_COLUMN_NUMBER = 25
MAX_ROW_NUMBER = 45

# Settaggio colori
window.color_options.addItem("Nessuno")
window.color_options.addItem("Rosso")
window.color_options.addItem("Arancione")
window.color_options.addItem("Giallo")
window.color_options.addItem("Verde")
window.color_options.addItem("Azzurro")
window.color_options.addItem("Blu")
window.color_options.addItem("Rosa")

color_blank = QColor(255,255,255)
color_red = QColor(255,0,0)
color_green = QColor(102,204,0)
color_cyan = QColor(0,204,204)
color_yellow = QColor(255,255,102)
color_pink = QColor(255,153,255)
color_orange = QColor(255,153,51)
color_blue = QColor(102,178,255)

# Dynamic Functions
cell_list_dynamic = []
window.color_options_dynamic.addItem("Verde")
window.color_options_dynamic.addItem("Rosso")
window.color_options_dynamic.addItem("Arancione")
window.color_options_dynamic.addItem("Giallo")
window.color_options_dynamic.addItem("Azzurro")
window.color_options_dynamic.addItem("Blu")
window.color_options_dynamic.addItem("Rosa")

list_dynamic_functions = []



# Defs
def apply_text():
    reset_errors_and_warnings()

    text_bold = window.text_bold.isChecked()
    text_italic = window.text_italic.isChecked()
    text_underline = window.text_underline.isChecked()

    # Coordinates
    input_text_x = window.input_text_x.text()
    input_text_y = window.input_text_y.text()

    if input_text_x.isdigit()==False or input_text_y.isdigit()==False:
        error('You must write the coordinates as Digits!')

    column = ''
    row = ''
    if input_text_x != '':
        column = int(input_text_x) - 1
    if input_text_y != '':
        row = int(input_text_y) - 1
    item = window.tableWidget.item(row, column)
    if item is None:
        item = QTableWidgetItem("Testo")
        window.tableWidget.setItem(row, column, item)

    font = item.font()
    font.setBold(text_bold)
    font.setItalic(text_italic)
    font.setUnderline(text_underline)

    item.setFont(font)

    # Clear
    window.input_text_x.setText('')
    window.input_text_y.setText('')

    return
    

def apply_color():
    reset_errors_and_warnings()

    CHOSEN_COLOR = window.color_options.currentText()
    if CHOSEN_COLOR == "Nessuno":
        COLOR = color_blank
    elif CHOSEN_COLOR == "Rosso":
        COLOR = color_red
    elif CHOSEN_COLOR == "Arancione":
        COLOR = color_orange
    elif CHOSEN_COLOR == "Giallo":
        COLOR = color_yellow
    elif CHOSEN_COLOR == "Verde":
        COLOR = color_green
    elif CHOSEN_COLOR == "Azzurro":
        COLOR = color_cyan
    elif CHOSEN_COLOR == "Blu":
        COLOR = color_blue
    elif CHOSEN_COLOR == "Rosa":
        COLOR = color_pink
    
        

    color_row = window.color_row.isChecked()
    color_cell = window.color_cell.isChecked()
    color_column = window.color_column.isChecked()

    if color_row==False and color_cell==False and color_column==False:
        warning('Select an Option to proceed: CELL, ROW or COLUMN')

    # Coordinates
    input_color_x = window.input_color_x.text()
    input_color_y = window.input_color_y.text()

    column = ''
    row = ''
    if input_color_x != '':
        warning_coordinates = False
        if input_color_x.isdigit():
            column = int(input_color_x) - 1
        else:
            error('You must write the coordinates as Digits!')
    else:
        warning_coordinates = True
    if input_color_y != '':
        warning_coordinates = False
        if input_color_y.isdigit():
            row = int(input_color_y) - 1
        else:
            error('You must write the coordinates as Digits!')
    else:
        warning_coordinates = True
    
    if warning_coordinates:
        warning('Specify the coordinates X,Y for the CELL and just one for ROW and COLUMN')

    if color_cell:
        item = window.tableWidget.item(row, column)
        if item is None:
            item = QTableWidgetItem("")
            window.tableWidget.setItem(row, column, item)
        item.setBackground(COLOR)
    else:
        number = 0
        # O color_row o color_column
        if column != '':
            number = column
        elif row != '':
            number = row

        if color_row:
            custom_row = number
            custom_column = 0
            for custom_column in range(0,MAX_COLUMN_NUMBER,1):
                item = window.tableWidget.item(custom_row, custom_column)
                if item is None:
                    item = QTableWidgetItem("")
                    window.tableWidget.setItem(custom_row, custom_column, item)
                item.setBackground(COLOR)

        elif color_column:
            custom_column = number
            custom_row = 0
            for custom_row in range(0,MAX_ROW_NUMBER,1):
                item = window.tableWidget.item(custom_row, custom_column)
                if item is None:
                    item = QTableWidgetItem("")
                    window.tableWidget.setItem(custom_row, custom_column, item)
                item.setBackground(COLOR)

    # Clear
    window.input_color_x.setText('')
    window.input_color_y.setText('')
   
    return


def apply_static():

    reset_errors_and_warnings()

    # Celle
    first_cell_raw = window.dynamic_first.text()
    second_cell_raw = window.dynamic_second.text()
    result_cell_raw = window.dynamic_result.text()

    if first_cell_raw == '' or second_cell_raw == '' or result_cell_raw == '':
        warning("One or more cell's coordinates are missing")

    first_cell_str = first_cell_raw.split()
    second_cell_str = second_cell_raw.split()
    result_cell_str = result_cell_raw.split()

    if len(first_cell_str) != 2 or len(second_cell_str) != 2 or len(result_cell_str) != 2:
        error('The coordinates must be written as X Y! You have written a different amount of coordinates.')

    
    cell_list = []
    cell_list.append(int(first_cell_str[0]))
    cell_list.append(int(first_cell_str[1]))
    cell_list.append(int(second_cell_str[0]))
    cell_list.append(int(second_cell_str[1]))
    cell_list.append(int(result_cell_str[0]))
    cell_list.append(int(result_cell_str[1]))

    for cell_item in cell_list:
        if str(cell_item).isdigit() == False:
            error("Cell's coordinates Must be number written as X Y. Example: 1 2")

    print(cell_list)


    # Funzione scelta
    fun_sum = window.dynamic_sum.isChecked()
    fun_subdivide = window.dynamic_subdivide.isChecked()
    fun_moltiplicate = window.dynamic_moltiplicate.isChecked()
    fun_divide = window.dynamic_divide.isChecked()
    fun_is_equal = window.dynamic_is_equal.isChecked()
    fun_is_greater = window.dynamic_is_greater.isChecked()
    fun_is_less = window.dynamic_is_less.isChecked()
    fun_compare_as_text = window.dynamic_compare_as_text.isChecked()


    # Prima cella
    first_item = window.tableWidget.item(cell_list[1]-1, cell_list[0]-1)
    if first_item is None:
        error('The first cell is empty! Insert a value before proceeding.')
        first_item = QTableWidgetItem("")
    first_cell_value = first_item.text()

    # Seconda cella
    second_item = window.tableWidget.item(cell_list[3]-1, cell_list[2]-1)
    if second_item is None:
        error('The second cell is empty! Insert a value before proceeding.')
        second_item = QTableWidgetItem("")
    second_item_value = second_item.text()
    
    result = ''

    if fun_sum:
        result = int(first_cell_value) + int(second_item_value)
        print(result)
    elif fun_subdivide:
        result = int(first_cell_value) - int(second_item_value)
        print(result)
    elif fun_moltiplicate:
        result = int(first_cell_value) * int(second_item_value)
        print(result)
    elif fun_divide:
        result = int(first_cell_value) / int(second_item_value)
        print(result)
    elif fun_is_equal:
        if first_cell_value == second_item_value:
            result = True
        else:
            result = False
        print(result)
    elif fun_is_greater:
        if int(first_cell_value) > int(second_item_value):
            result = True
        else:
            result = False
        print(result)
    elif fun_is_less:
        if int(first_cell_value) < int(second_item_value):
            result = True
        else:
            result = False
        print(result)
    elif fun_compare_as_text:
        if int(first_cell_value) < int(second_item_value):
            result = ':LOWER:'
        elif int(first_cell_value) > int(second_item_value):
           result = ':GREATER:'
        else:
            result = ':EQUAL:'
        print(result)
    else:
        warning('You must select a function before clicking Apply')
    
    item_result = QTableWidgetItem(str(result))
    window.tableWidget.setItem(cell_list[5]-1, cell_list[4]-1, item_result)

    # Clear list
    cell_list.clear()

    return


def apply_dynamic():

    reset_errors_and_warnings()

    # Celle
    first_cell_raw = window.dynamic_first.text()
    second_cell_raw = window.dynamic_second.text()
    result_cell_raw = window.dynamic_result.text()

    if first_cell_raw == '' or second_cell_raw == '' or result_cell_raw == '':
        warning("One or more cell's coordinates are missing")

    first_cell_str = first_cell_raw.split()
    second_cell_str = second_cell_raw.split()
    result_cell_str = result_cell_raw.split()

    if len(first_cell_str) != 2 or len(second_cell_str) != 2 or len(result_cell_str) != 2:
        error('The coordinates must be written as X Y! You have written a different amount of coordinates.')
        return # Rischio corruzione lista sottostante

    try:
        cell_list_dynamic.append(int(first_cell_str[0]))
        cell_list_dynamic.append(int(first_cell_str[1]))
        cell_list_dynamic.append(int(second_cell_str[0]))
        cell_list_dynamic.append(int(second_cell_str[1]))
        cell_list_dynamic.append(int(result_cell_str[0]))
        cell_list_dynamic.append(int(result_cell_str[1]))
    except:
        error("Cell's coordinates Must be number written as X Y. Example: 1 2")

    for cell_item in cell_list_dynamic:
        if str(cell_item).isdigit() == False and 'fun_' not in str(cell_item):
            print(cell_item)
            error("Cell's coordinates Must be number written as X Y. Example: 1 2")
            

    print(cell_list_dynamic)


    # Funzione scelta
    fun_sum = window.dynamic_sum.isChecked()
    fun_subdivide = window.dynamic_subdivide.isChecked()
    fun_moltiplicate = window.dynamic_moltiplicate.isChecked()
    fun_divide = window.dynamic_divide.isChecked()
    fun_is_equal = window.dynamic_is_equal.isChecked()
    fun_is_greater = window.dynamic_is_greater.isChecked()
    fun_is_less = window.dynamic_is_less.isChecked()
    fun_compare_as_text = window.dynamic_compare_as_text.isChecked()


    # Prima cella
    first_item = window.tableWidget.item(cell_list_dynamic[-5]-1, cell_list_dynamic[-6]-1)
    if first_item is None:
        error('The first cell is empty! Insert a value before proceeding.')
        first_item = QTableWidgetItem("")
    first_cell_value = first_item.text()

    # Seconda cella
    second_item = window.tableWidget.item(cell_list_dynamic[-3]-1, cell_list_dynamic[-4]-1)
    if second_item is None:
        error('The second cell is empty! Insert a value before proceeding.')
        second_item = QTableWidgetItem("")
    second_item_value = second_item.text()
    
    result = ''

    if fun_sum:
        result = int(first_cell_value) + int(second_item_value)
        cell_list_dynamic.append('fun_sum')
        print(result)
    elif fun_subdivide:
        result = int(first_cell_value) - int(second_item_value)
        cell_list_dynamic.append('fun_subdivide')
        print(result)
    elif fun_moltiplicate:
        result = int(first_cell_value) * int(second_item_value)
        cell_list_dynamic.append('fun_moltiplicate')
        print(result)
    elif fun_divide:
        result = int(first_cell_value) / int(second_item_value)
        cell_list_dynamic.append('fun_divide')
        print(result)
    elif fun_is_equal:
        if first_cell_value == second_item_value:
            result = True
        else:
            result = False
        cell_list_dynamic.append('fun_is_equal')
        print(result)
    elif fun_is_greater:
        if int(first_cell_value) > int(second_item_value):
            result = True
        else:
            result = False
        cell_list_dynamic.append('fun_is_greater')
        print(result)
    elif fun_is_less:
        if int(first_cell_value) < int(second_item_value):
            result = True
        else:
            result = False
        cell_list_dynamic.append('fun_is_less')
        print(result)
    elif fun_compare_as_text:
        if int(first_cell_value) < int(second_item_value):
            result = ': LOWER :'
        elif int(first_cell_value) > int(second_item_value):
           result = ': GREATER :'
        else:
            result = ': EQUAL :'
        cell_list_dynamic.append('fun_compare_as_text')
        print(result)
    else:
        warning('You must select a function before clicking Apply')
        cell_list_dynamic.append('fun_ignore_items')
        return
    
    item_result = QTableWidgetItem(str(result))
    window.tableWidget.setItem(cell_list_dynamic[-2]-1, cell_list_dynamic[-3]-1, item_result)

    print(cell_list_dynamic)


    # Colorazione cella
    CHOSEN_COLOR = window.color_options_dynamic.currentText()
    COLOR = ''
    if CHOSEN_COLOR == "Nessuno":
        COLOR = color_blank
    elif CHOSEN_COLOR == "Rosso":
        COLOR = color_red
    elif CHOSEN_COLOR == "Arancione":
        COLOR = color_orange
    elif CHOSEN_COLOR == "Giallo":
        COLOR = color_yellow
    elif CHOSEN_COLOR == "Verde":
        COLOR = color_green
    elif CHOSEN_COLOR == "Azzurro":
        COLOR = color_cyan
    elif CHOSEN_COLOR == "Blu":
        COLOR = color_blue
    elif CHOSEN_COLOR == "Rosa":
        COLOR = color_pink

    item = window.tableWidget.item(cell_list_dynamic[-2]-1, cell_list_dynamic[-3]-1)
    item.setBackground(COLOR)


    # Aggiunta in list_dynamic_functions
    FUNCTION_INFO_LIST = cell_list_dynamic
    FUNCTION_INFO = []

    while 1:
        partial_info = ''
        for item in FUNCTION_INFO_LIST:
            partial_info+=item
            if 'fun_' in item:
                FUNCTION_INFO.append(partial_info)
                partial_info = ''

    
    window.list_dynamic_functions.setText(FUNCTION_INFO)

    return


def refresh_all_dynamic():

    reset_errors_and_warnings()

    for index in range(0,len(cell_list_dynamic),7):
        # Prima cella
        first_item = window.tableWidget.item(cell_list_dynamic[index+1]-1, cell_list_dynamic[index]-1)
        first_cell_value = first_item.text()

        # Seconda cella
        second_item = window.tableWidget.item(cell_list_dynamic[index+3]-1, cell_list_dynamic[index+2]-1)
        second_cell_value = second_item.text()

        # Funzione
        fun_name = cell_list_dynamic[index+6]

        result = ''

        if fun_name=='fun_sum':
            result = int(first_cell_value) + int(second_cell_value)
            print(result)
        elif fun_name=='fun_subdivide':
            result = int(first_cell_value) - int(second_cell_value)
            print(result)
        elif fun_name=='fun_moltiplicate':
            result = int(first_cell_value) * int(second_cell_value)
            print(result)
        elif fun_name=='fun_divide':
            result = int(first_cell_value) / int(second_cell_value)
            print(result)
        elif fun_name=='fun_is_equal':
            if first_cell_value == second_cell_value:
                result = True
            else:
                result = False
            print(result)
        elif fun_name=='fun_is_greater':
            if int(first_cell_value) > int(second_cell_value):
                result = True
            else:
                result = False
            print(result)
        elif fun_name=='fun_is_less':
            if int(first_cell_value) < int(second_cell_value):
                result = True
            else:
                result = False
            print(result)
        elif fun_name=='fun_compare_as_text':
            if int(first_cell_value) < int(second_cell_value):
                result = ': LOWER :'
            elif int(first_cell_value) > int(second_cell_value):
                result = ': GREATER :'
            else:
                result = ': EQUAL :'
            print(result)
        else:
            pass # Significa che prima c'era stato un errore
        
        item_result = QTableWidgetItem(str(result))
        window.tableWidget.setItem(cell_list_dynamic[index+5]-1, cell_list_dynamic[index+4]-1, item_result)
    
    return


    
    
   




def warning(WARNING_MESSAGE: str):
    current_text = window.errors_and_warnings.text()
    message = current_text + '<br>' + 'WARNING: ' + WARNING_MESSAGE + '<br>'
    window.errors_and_warnings.setText(message)

def error(ERROR_MESSAGE: str):
    current_text = window.errors_and_warnings.text()
    message = current_text + '<br>' + 'ERROR: ' + ERROR_MESSAGE  + '<br>'
    window.errors_and_warnings.setText(message)

def reset_errors_and_warnings():
    window.errors_and_warnings.setText('')



window.color_apply.clicked.connect(apply_color)
window.text_apply.clicked.connect(apply_text)

window.dynamic_apply_static.clicked.connect(apply_static)
window.dynamic_apply_dynamic.clicked.connect(apply_dynamic)
window.refresh_all_dynamic.clicked.connect(refresh_all_dynamic)
refresh_all_dynamic



window.show()
sys.exit(app.exec())