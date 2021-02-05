import sqlite3
from tkinter import *
from consts import *

class Questions:
    
    def __init__(self):
        self.id_pregunta = 1
        self.respuesta = 0  
        self.questions = ()
        self.answers = ()
        self.imagenes = {6:"img/preguntas/matriz0.png",
                        7:"img/preguntas/matriz1.png", 
                        10:"img/preguntas/matriz2.png",
                        12:"img/preguntas/matriz3.png"}
        self.height = HEIGHT_QUESTIONS
        self.row = 1

    def listarPreguntas(self):
        self.conexiondb = sqlite3.connect('db/database.db')
        self.cursor = self.conexiondb.cursor()
        self.cursor.execute("SELECT * FROM questions where id_pregunta = {0}".format(self.id_pregunta))
        self.questions = self.cursor.fetchone()
        self.cursor.execute("SELECT * FROM answers where id_pregunta = {0}".format(self.id_pregunta))
        self.answers = self.cursor.fetchall()
        if self.questions is None:
            self.id_pregunta = 1
            self.listarPreguntas()
        self.conexiondb.close()

    def configurarCajaPregunta(self, move):
        self.root = Tk()
        self.root.title(TITULO)
        self.root.iconbitmap("img/Escudo_ULibre.ico")
        _screen_width = self.root.winfo_screenwidth()
        _screen_height = self.root.winfo_screenheight()	
        self.x = (_screen_width/2)-(WIDTH_QUESTIONS/2)
        self.y= (_screen_height/2)-(self.height/2)
        self.height = HEIGHT_QUESTIONS
        if self.id_pregunta in self.imagenes.keys():
            self.height = 580
        self.root.geometry("%dx%d+%d+%d" % (WIDTH_QUESTIONS, self.height, self.x, self.y))
        self.root.config(bg="#008080", relief="groove", bd=10)
        self.dibujarCajaPreguntas(move)

    def cerrarPregunta(self):
        self.root.destroy()
    
    def seleccionar(self):
        print(self.opcion.get())

    def dibujarCajaPreguntas(self, move):
        _temp = ''
        self.opcion = IntVar()
        if len(self.questions[1]) >= 98:
            if round(len(self.questions[1])/98, 0) == 1:
                _temp = self.questions[1][0:98]+'\n'+self.questions[1][98:len(self.questions[1])]
            elif round(len(self.questions[1])/98, 0) == 2:
                _temp = self.questions[1][0:98]+'\n'+self.questions[1][98:196]+'\n'+\
                    self.questions[1][196:len(self.questions[1])]
            else:
                _temp = self.questions[1][0:98]+'\n'+self.questions[1][98:196]+'\n'+\
                    self.questions[1][196:294]+'\n'+self.questions[1][294:len(self.questions[1])]
        else:
            _temp = self.questions[1]
        Label(self.root, text=_temp, bg="#1EEEEA", fg="blue",\
            font=("Black", 12, "bold")).pack()
        self.miFrame = Frame(self.root)
        self.miFrame.config(bg="#008080", width=WIDTH_QUESTIONS, height=self.height)
        if self.id_pregunta in self.imagenes.keys():
            _imagen = PhotoImage(file=self.imagenes[self.id_pregunta])
            Label(self.miFrame, image=_imagen).pack(pady=8, ipadx=8)
        else:
            self.row = 0
        for array, data in enumerate(self.answers):
            Radiobutton(self.miFrame, text=data[1], variable=self.opcion, bg="#008080", value=data[0], \
                command=self.seleccionar, font=("Black", 11)).pack(pady=5, ipadx=5)
            self.row += array+1
        Button(self.miFrame, text="Ok", command=self.cerrarPregunta, width=12).pack(pady=5, ipadx=5)
        self.miFrame.pack(fill="both", expand=True)
        self.root.mainloop()
        self.respuesta = self.opcion.get()
        self.respuesta = self.estadoMove(move)

    def estadoMove(self, move):
        self.value = move
        if self.respuesta == self.questions[2]:
            pass
        else:
            if self.value == 1:
                self.value = 2
            else:
                self.value = 1
        self.id_pregunta+=1
        return self.value
    
    def preguntar(self, move):
        self.listarPreguntas()
        self.configurarCajaPregunta(move)
        return self.respuesta
