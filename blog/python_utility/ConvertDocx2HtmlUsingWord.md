---
layout: default
titel: Python��RPA���������悤(��1��:Word���g�p�����t�@�C���ϊ�)
description: Word���g�p����docx�t�@�C����HTML��PDF�ɕϊ��Bwin32com�BRPA�B
lang: ja_JP
---
## Python��RPA���������悤(��1��:Word���g�p�����t�@�C���ϊ�)

����ɂ��́Anetchira�ł��B

�F�����Python��win32com�Ƃ������C�u�����������m�ł����H
COM�C���^�[�t�F�[�X�o�R��PC�ɃC���X�g�[������Ă���A�v���P�[�V�������N���A�I���A�����Ċe�푀����s�����Ƃ��\�ł��B
�����Microsoft Word��win32com�Ő��䂵�A�u�����͎��Ƃł���Ă��邱�Ƃ��X�N���v�g�ŋL�q���Ď������v���������Ǝv���܂��B

### COM�Ƃ�
�uCOM �Ƃ́v�ƃO�O�b�Ă݂Ă��������B�F��ȏ�񂪌����邩�Ǝv���܂��B
���Ȃ�ɂ��������������ƁAWindows�œ��삷��A�v���P�[�V����������Ƃ��ɗ\�ߊO��������Ăт�����悤�ɕ����I�ɋ@�\���R���|�[�l���g�������Ă����Z�p�̂��Ƃł��B
Python�ł͕W�����C�u�����Ƃ���win32com���p�ӂ���Ă���A����ɂ��COM�C���^�[�t�F�[�X�o�R��Windows�A�v���P�[�V�������O�����琧��ł��܂��B

### ����̎������l�^
����́AMicrosoft Word���g�p����docx�t�@�C����HTML�`����PDF�`���ɂ��āu���O��t���ĕۑ��v�������Ƃ��������������Ǝv���܂��B

�F�����Word�ō쐬����������PDF�������Ƃ͂�������Ƃ���܂���ˁH

![main_window](../picture/ConvertDocx2HtmlUsingWord/WordSaveAs2.PNG)


����ł��B

�܂��A���������������Python�X�N���v�g��p�ӂ��āA�ǂ�ȃ����b�g������񂾁H���Ċ����ł����A�Ƃ肠�����Љ�܂��B

### Python�X�N���v�g
�ȉ��Adocx��HTML�ɕϊ�����Python�X�N���v�g(�֐�)�ł��B

{% highlight <Python> [linenos] %}

def ConvertDocx2HtmlUsingWord(DocxFilePath):
    import win32com.client
    import os

    # �t�@�C���g���q�̊m�F
    if os.path.exists(DocxFilePath) and (DocxFilePath[-5:] == ".docx"):
        # �t�@�C���p�X����g���q(�s���I�h�܂�5������)����菜��
        str_FilePathNoExt = DocxFilePath[0:-5]
        # �t�@�C���̊g���q�Ƃ���".htm"��t�^
        str_HtmlFilePath = str_FilePathNoExt + ".htm"
        # �t�@�C���p�X�Ƃ��Đ���
        HtmlFilePath = os.path.abspath(str_HtmlFilePath)
    else:
        raise UserWarning("File Format is not .docx")
    
    # Word���N������ : Application�I�u�W�F�N�g�𐶐�����
    Application = win32com.client.Dispatch("Word.Application")

    # Word����ʕ\������ : Visible�v���p�e�B��True�ɂ���
    Application.Visible = True

    # �����������J��
    doc = Application.Documents.Open(DocxFilePath)

    # ���O��t���ĕۑ� : �t�@�C���`����[Web�y�[�W(�t�B���^�[��)]�Ɏw��
    WdFormatHTML = 8
    WdFormatFilteredHTML = 10
    doc.SaveAs2(HtmlFilePath, FileFormat=WdFormatFilteredHTML)

    # ���������
    doc.Close()

    # Word���I������ : Quit���\�b�h���Ă�
    Application.Quit()

{% endhighlight %}


������SaveAs2�Ƃ����֐����o�ꂵ�Ă���̂ł����AFileFormat�Ƃ��������ɂ͐���(�萔)���w�肷��ΐF��ȃt�@�C���`����I�ׂ܂��B

���̒萔�ɂ��Ă̎d�l�͉��L��web�y�[�W�ɋL�ڂ���Ă��܂��B

[Microsoft VBA���t�@�����X WdSaveFormat](https://docs.microsoft.com/ja-jp/office/vba/api/word.wdsaveformat)

���Ȃ݂ɁASaveAs2�֐���FileFormat�Ƃ������������݂��邱�Ƃ́A���L��web�y�[�W���甭�����܂����B�����������Љ�B

[Python Programming](https://en.m.wikibooks.org/wiki/Python_Programming/MS_Word)

�����̏�����肷��̂ɁA���Ԃ�������܂����c

### �Ȃ�HTML�ɕϊ�����X�N���v�g���ɂ��������H
��������͏����]�k�ł��B
Word �t�@�C���ɍ쐬���ꂽ�I�[�g�V�F�C�v(�}�`)��L�����o�X���āAHTML������ƑS�ĉ摜�t�@�C���`��(png)�Ő��������̂ł��B
Word�ō쐬�����}�`����ŕʂ̗p�r�Ɏg���ꍇ�A�����葁���ł��B


### RPA���āA�ǂ����H
����ŁARPA���������邽�߂̃A�v���P�[�V�����́u�p�[�c�v����ꂽ���ȁA�Ǝv���Ă��܂��B
���̒��Ŕ̔�����Ă���RPA(���Ƃ���[�R��](https://www.celf.biz/rpa/)�Ƃ�)�Ɣ�ׂ�ƁA������Word�̃t�@�C���ϊ��������A�Ƃ������x�����Ǝv���܂����A���������̂������ς�����Ă�����RPA�ł���̂ł́H�ƌl�I�Ɋ��҂��Ă��܂��B

�ȏ�ł��B
