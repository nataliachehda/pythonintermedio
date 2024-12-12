import tkinter as tk
from cliente.vista import Frame,barrita_menu

def main(): 
    ventana = tk.Tk()
    ventana.title('Lista Perros')
    
    ventana.resizable(False,False)

    barrita_menu(ventana)
    app = Frame(root=ventana)

    ventana.mainloop()
    
if __name__ == '__main__':
    main()
