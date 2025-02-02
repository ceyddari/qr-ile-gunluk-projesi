**Adding a journal:** Run `python main.py`, select the **Add a new journal** option, write and save your journal; a hidden file with a UUID is created, and a QR code is generated. It is stored securely on the computer, and no one can open the journal without the QR code.  

**Listing journals:** Run `python main.py`, select the **List journals** option, and view all saved journals with their UUID file names.  

**Opening a journal (manually):** Run `python main.py`, select the **Open journal** option, enter the listed UUID file name, and the journal will open in Notepad.  

**Opening a journal (using QR code):** Run `python qr_oku.py gizli_gunlukler/QR_KOD.png`, scan the QR code, and the journal will open automatically.  

**Editing or deleting a journal:** Journals can be edited in Notepad or manually deleted from the hidden folder. Deleted journals cannot be recovered.
