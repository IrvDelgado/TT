import ebooklib
from ebooklib import epub
import html2text
import os

libros=[f for f in os.listdir(os.curdir) if os.path.isfile(f)]
for libro in libros:
    print("Working with file "+ libro)
    if(libro!='getTextBooks.py'):
        nombrecarpeta=libro[:-5]
        
        if(not os.path.isdir(nombrecarpeta)):
            #crear carpeta
            os.mkdir(nombrecarpeta)

            book = epub.read_epub(libro)

            for item in book.get_items():
                if item.get_type() == ebooklib.ITEM_DOCUMENT:
                    
                    #asi se llamara el archivo. item.get_name()
                    filename=item.get_name()[5:] 
                    f=open(nombrecarpeta+'/'+filename,"w")
                    f2=open(nombrecarpeta+'/'+filename[:-4]+'txt',"w")

                    #este es el contenido del archivo.  (probar con get_content y get_body_content)
                    f.write(item.get_content().decode("utf-8"))
                    f2.write( html2text.html2text(item.get_content().decode("utf-8")))                    

                    f.close() 
                    f2.close()
        else:
            print("no creando carpeta "+ libro)