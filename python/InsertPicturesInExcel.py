# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 20:28:35 2017
Spyderエディタ
For Python 2.7
@author: netchira
"""
import os
import Tkinter      #GUIコントロール
import ttk          #GUIコントロール(Combobox)
import tkFileDialog #ファイル操作
import tkMessageBox #メッセージボックス表示
import openpyxl as px
from openpyxl.drawing.image import Image
import PIL.Image
import numpy as np
import re
from glob import glob

#スクリプトの開始
print "Insert Pictures In Excel Start"

#root定義
root = Tkinter.Tk()
root.title(u"画像ファイル自動挿入スクリプト")
root.geometry("600x180")

#root上のグローバル変数定義
g_PictureType =Tkinter.StringVar()
g_PictureType.set('type')#変数の初期化
g_ExcelFile =Tkinter.StringVar()
g_ExcelFile.set('file_name(output)')#変数の初期化
g_PictFolderPath =Tkinter.StringVar()
g_PictFolderPath.set('folder_name(input)')#変数の初期化
g_SelectedSheet =Tkinter.StringVar()
g_SelectedSheet.set('nothing')#変数の初期化

g_PictSizeWidth =Tkinter.StringVar()
g_PictSizeWidth.set('500')#変数の初期化
g_PictSizeHeight =Tkinter.StringVar()
g_PictSizeHeight.set('500')#変数の初期化
g_PictPosition =Tkinter.StringVar()
g_PictPosition.set('A10,L11')#変数の初期化

g_ExcelSheets = ('A', 'B', 'C') #tuple 初期化

#色の定義
BLACK = '#000000'
RED = '#ff0000'
PINK = '#ffaacc'

"""
 呼び出し元：ボタン1
 関数の処理内容：Excelファイルを選択する
"""
def SelectExcelFile(event):
    global g_ExcelFile
    #ファイルを選択する
    fTyp = [("xlsxファイル",".xlsx"),("xlsファイル",".xls"),("すべてのファイル",".*")]
    iDir = os.path.abspath(os.path.curdir)
    #tkMessageBox.showinfo('Excelファイル選択','ファイルを選択してください。')
    filepath = tkFileDialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    if filepath != "":
        g_ExcelFile.set(filepath)
        Entry1.configure(textvariable = g_ExcelFile)
    
    #シート名を抽出
    if os.path.exists(filepath):
        wb = px.load_workbook(filepath)
        sheet_list = wb.get_sheet_names()
        sheet_tuple = tuple(sheet_list)
        g_ExcelSheets = sheet_tuple
        print g_ExcelSheets
    else:
        g_ExcelSheets = ('A', 'B', 'C')
    
    # Combobox の選択項目を更新
    Combobox2['values'] = g_ExcelSheets

"""
 呼び出し元：ボタン2
 関数の処理内容：画像ファイルが格納されているフォルダを選択する
"""
def SelectFolder(event):
    global g_PictFolderPath
    #フォルダを選択する
    iDir = os.path.abspath(os.path.curdir)
    #tkMessageBox.showinfo('フォルダ選択','画像ファイルが格納されているフォルダを選択してください。')
    folderpath = tkFileDialog.askdirectory(initialdir = iDir)
    if folderpath != "":
    g_PictFolderPath.set(folderpath)
    Entry2.configure(textvariable = g_PictFolderPath)
    
"""
 呼び出し元：ボタン3
 関数の処理内容：Excelファイルに画像を挿入する
"""
def InsertPictureFiles(event):
    global g_ExcelFile
    global g_PictFolderPath
    global g_PictureType
    global g_SelectedSheet
    
    l_file   = g_ExcelFile.get()
    l_folder = g_PictFolderPath.get()
    l_type   = g_PictureType.get()
    l_selectedsheet = g_SelectedSheet.get()
    l_pic_position = g_PictPosition.get()
    
    #ファイルの所在の確認
    l_flag1 = os.path.exists(l_file)
    l_flag2 = os.path.exists(l_folder)
   
    if l_flag1 and l_flag2:   
        # 画像の一時保存用フォルダを作成する
        temp_folder = l_folder + u"/TempForPython"
        if not os.path.exists(temp_folder):
            os.mkdir(temp_folder)
            
        # Excelファイルを開く
        wb = px.load_workbook(l_file)

        # シートを指定する
        ws = wb.get_sheet_by_name(l_selectedsheet)
        
        # 画像ファイルのみのリストを作成する(拡張子はユーザーが指定したもの)
        picts_path = l_folder + '/*'
        picts_path += l_type
        picts_list = glob(picts_path)
        
        # 画像の挿入位置の算出
        picts_num = len(picts_list)
        position_list = CalculatePosition(l_pic_position, picts_num)

        # xlsxファイルの編集処理
        for index, pict in enumerate(picts_list):        
            # 画像の編集
            PictureSizeConversion(pict, temp_folder)
            
            # 画像ファイル名の挿入
            filename_pos = position_list[index]
            ws[filename_pos] = GetFileName(pict)
            
            # 画像の挿入
            image_pos = CellRowIncrement(position_list[index])
            new_pic_path = temp_folder +  "/" + os.path.basename(pict)
            temp_img = Image(new_pic_path)
            ws.add_image(temp_img, image_pos)
            
        # 新しいxlsxファイルを保存
        temp_filename = GetFileName(l_file)
        temp_filename = l_folder + "/" + temp_filename 
        newwb = temp_filename  + "_new.xlsx"
        wb.save(newwb)
        
        # メッセージ表示
        print "Insert Pictures Success!"
        dispmsg = u"Excelファイルに画像を挿入しました。ベースとなったExcelファイルと同じディレクトリに新しいExcelファイルを出力しました。\n"
        dispmsg += u"また、一時的にサイズを変更した画像ファイルをTempForPythonフォルダに格納しています。不要であれば削除してください。\n"
        tkMessageBox.showinfo('Success', dispmsg)

    elif l_flag2:
        # エラー表示：存在していないファイル名の指定
        dispmsg = u"下記ファイルが存在していませんでした。再度、ファイルを選択してください。\n"
        dispmsg += (l_file + "\n")
        tkMessageBox.showinfo('Excelファイルが見つかりません', dispmsg)

    elif l_flag1:
        # エラー表示：存在していないフォルダ名の指定
        dispmsg = u"選択したフォルダが存在していませんでした。再度、フォルダを選択してください。\n"
        dispmsg += (l_folder + "\n")
        tkMessageBox.showinfo('画像を格納したフォルダが見つかりません', dispmsg)
    
    else :
        tkMessageBox.showinfo('スクリプトが実行できません', "ファイル名、フォルダを正しく指定してください。\n")


"""
 関数の処理内容：英字だけを抽出し、リストで返す。([a-zA-Z]は正規表現)
"""
def get_alphabet_list(text):
    matchedList = re.findall('[a-zA-Z]',text)
    return matchedList

"""
 関数の処理内容：数字だけを抽出し、リストで返す。([0-9]は正規表現)
"""
def get_number_list(text):
    temp = re.findall('[0-9]*',text)
    numberList = filter(None, temp)
    return numberList

"""
 関数の処理内容：PILライブラリを使って画像のサイズを変更し、新しいファイルとして保存する
"""
def PictureSizeConversion(pic_path, hozon_directory):
    global g_PictSizeHeight
    global g_PictSizeWidt
    
    # 変更したい画像サイズの取得
    l_pic_height = g_PictSizeHeight.get()
    l_pic_width  = g_PictSizeWidth.get()
    intHeight = int(l_pic_height)
    intWidth  = int(l_pic_width)
    
    # 画像のサイズ変更(PILライブラリ)
    origin_pic_path = pic_path
    img_raw = PIL.Image.open(origin_pic_path)
    img_copy = img_raw.copy()
    img_resize = img_copy.resize((intWidth, intHeight), PIL.Image.LANCZOS)
    
    # 画像の保存
    new_pic_path = hozon_directory + "/" + os.path.basename(pic_path)
    img_resize.save(new_pic_path)

"""
 関数の処理内容：画像を挿入するセルの位置を算出する
"""
def CalculatePosition(base_position, picts_num):   
    global g_PictSizeHeight
    
    # 画像のサイズからExcel何行分に相当するか算出
    l_pic_height = g_PictSizeHeight.get()
    intHeight = int(l_pic_height)
    pict_height = intHeight / 16
    
    # ユーザーが指定した挿入位置の決定するために、行列を作成して何行何列か算出する
    split_str_list = base_position.split(',')
    row = len(split_str_list)
    
    if picts_num % row == 0:
        collumn = picts_num / row
    else:
        collumn = picts_num / row + 1     
    
    # ユーザーが指定したセル位置の列数のみ(数字部分のみ)を取得し、NumPy行列の生成
    number_list = get_number_list(base_position)
    nparray = np.array(number_list, dtype = 'int64')
    
    # NumPy行列を必要列数分リピートする。
    new_array = np.tile(nparray, collumn)
    
    # 画像を張り付ける2行目以降の位置を決定
    max_heght = pict_height * collumn
    pict_scale = np.arange(0, max_heght, pict_height)
    number_array = pict_scale.repeat(row)
    
    # 行列の加算、リストへの変換
    target_array = new_array + number_array
    target_list = target_array.tolist()
    
    # str型に変換
    result_sono1= []
    for content in target_list:
        result_sono1.append(str(content))
        
    # 半角英字だけ抽出
    text_list = get_alphabet_list(base_position)
    result_sono2= []
    for x in range(0, collumn):
        for index in range(0, row):
            result_sono2.append(text_list[index])
    
    # 最終的な結果を算出
    result = []
    if len(result_sono1) == len(result_sono2):
        for index in range(0, len(result_sono1)):
            result.append(result_sono2[index] + result_sono1[index])
    else:
        result = None
    
    # リストの要素数を、画像の個数分だけに絞る
    result = result[:picts_num]
    
    print result
    return result

"""
 関数の処理内容：セルの位置(行のみ)をインクリメントする
"""
def CellRowIncrement(cell):
    collumn = get_alphabet_list(cell)
    row_old = get_number_list(cell)
    
    # 行の値だけインクリメントし、セル位置を新しく文字列で生成
    incremented = int(row_old[0]) + 1
    row_new = str(incremented)
    cell_new = collumn[0] + row_new
    return cell_new

"""
関数の処理内容：ファイルのフルパスから拡張子を除いたファイル名だけを返す
"""
def GetFileName(file_path):
    file_name_ext = os.path.basename(file_path)
    temp = file_name_ext.split(".")
    file_name = temp[0] # 拡張子のないファイル名を取得
    return file_name



#ラベル1(textblock)を配置
dispmsg = u"Excelファイルと、画像ファイルが格納されたフォルダを選択してください。その後、画像挿入をクリックしてください。"
Label1 = Tkinter.Label(text=dispmsg, foreground=BLACK, background=PINK)
Label1.place(x=0, y=0)

#ラベル2(textblock)を配置
Label2 = Tkinter.Label(text=u'拡張子：', width=10, anchor=Tkinter.W)
Label2.place(x=30, y=30)

#ラベル3(textblock)を配置
Label3 = Tkinter.Label(text=u'サイズ縦：', width=10, anchor=Tkinter.W)
Label3.place(x=210, y=30)

#ラベル4(textblock)を配置
Label4 = Tkinter.Label(text=u'サイズ横：', width=10, anchor=Tkinter.W)
Label4.place(x=370, y=30)

#ラベル3(textblock)を配置
Label3 = Tkinter.Label(text=u'シート名：', width=10, anchor=Tkinter.W)
Label3.place(x=30, y=90)

#ラベル4(textblock)を配置
Label4 = Tkinter.Label(text=u'挿入セル：', width=10, anchor=Tkinter.W)
Label4.place(x=210, y=90)

#ラベル4(textblock)を配置
Label5 = Tkinter.Label(text=u'(※コンマ(,)で区切ると複数列に挿入)')
Label5.place(x=340, y=90)

#コンボボックス1(combobox)を配置
Combobox1= ttk.Combobox(width=10, textvariable=g_PictureType)
Combobox1.bind('<<ComboboxSelected>>')
Combobox1['values']=('.png','.jpeg','.bmp')
Combobox1.set('.png')
Combobox1.place(x=90, y=30)

#コンボボックス2(combobox)を配置
Combobox2= ttk.Combobox(width=10, textvariable=g_SelectedSheet)
Combobox2.bind('<<ComboboxSelected>>')
Combobox2['values']=g_ExcelSheets
Combobox2.set('')
Combobox2.place(x=90, y=90)

#ボタン1(button)を配置
Button1 = Tkinter.Button(width=10, text=u'ファイル選択')
Button1.bind("<ButtonRelease-1>",SelectExcelFile) #左クリックされると関数を呼び出すようにバインド
Button1.place(x=0, y=60)
    
#ボタン2(button)を配置
Button2 = Tkinter.Button(width=10, text=u'フォルダ指定')
Button2.bind("<ButtonRelease-1>",SelectFolder) #左クリックされると関数を呼び出すようにバインド
Button2.place(x=0, y=120)

#ボタン3(button)を配置
Button3 = Tkinter.Button(width=10, text=u'画像挿入')
Button3.bind("<ButtonRelease-1>",InsertPictureFiles) #左クリックされると関数を呼び出すようにバインド
Button3.place(x=0, y=150)
    
#エントリー1(textbox)を配置
Entry1 = Tkinter.Entry(width=80, textvariable=g_ExcelFile)
Entry1.place(x=90, y=60)

#エントリー2(textbox)を配置
Entry2 = Tkinter.Entry(width=80, textvariable=g_PictFolderPath)
Entry2.place(x=90, y=120)

#エントリー3(textbox)を配置
Entry3 = Tkinter.Entry(width=10, textvariable=g_PictSizeHeight)
Entry3.place(x=270, y=30)

#エントリー4(textbox)を配置
Entry4 = Tkinter.Entry(width=10, textvariable=g_PictSizeWidth)
Entry4.place(x=430, y=30)

#エントリー5(textbox)を配置
Entry5 = Tkinter.Entry(width=10, textvariable=g_PictPosition)
Entry5.place(x=270, y=90)


#mainloop
root.mainloop()
