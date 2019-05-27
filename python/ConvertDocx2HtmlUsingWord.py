# -*- coding: utf-8 -*-
"""
Created on Mon May 26 21:28:35 2019
Spyderエディタ
For Python ver 2.7
@author: netchira
"""
def ConvertDocx2HtmlUsingWord(DocxFilePath):
    import win32com.client
    import os

    # ファイル拡張子の確認
    if os.path.exists(DocxFilePath) and (DocxFilePath[-5:] == ".docx"):
        # ファイルパスから拡張子(ピリオド含む5文字分)を取り除く
        str_FilePathNoExt = DocxFilePath[0:-5]
        # ファイルの拡張子として".htm"を付与
        str_HtmlFilePath = str_FilePathNoExt + ".htm"
        # ファイルパスとして生成
        HtmlFilePath = os.path.abspath(str_HtmlFilePath)
    else:
        raise UserWarning("File Format is not .docx")
    
    # Wordを起動する : Applicationオブジェクトを生成する
    Application = win32com.client.Dispatch("Word.Application")

    # Wordを画面表示する : VisibleプロパティをTrueにする
    Application.Visible = True

    # 既存文書を開く
    doc = Application.Documents.Open(DocxFilePath)

    # 名前を付けて保存 : ファイル形式を[Webページ(フィルター後)]に指定
    WdFormatHTML = 8
    WdFormatFilteredHTML = 10
    doc.SaveAs2(HtmlFilePath, FileFormat=WdFormatFilteredHTML)

    # 文書を閉じる
    doc.Close()

    # Wordを終了する : Quitメソッドを呼ぶ
    Application.Quit()
