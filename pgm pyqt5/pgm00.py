#!/usr/bin/python3
# -*- coding: utf-8 -*-
# importaciones
import sys
import os
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5 import QtWidgets
from datetime import datetime

from pgm01 import *

# Clase vtnAgregar
class vtnAgrergar(QMainWindow):

    def __init__(self):
        super().__init__()

        self.inciaVTN()

    def inciaVTN(self):
        self.sal = qApp.quit
        # Mensaje de ventana
        QToolTip.setFont(QFont('SansSerif', 10))
        
        # Barra superior
        salirB = QAction('&Salir', self)
        salirB.setShortcut('Ctrl+Q')
        salirB.setStatusTip('Saldras del programa...')
        salirB.triggered.connect(self.salida)

        buscaB = QAction('Buscar', self)
        buscaB.setShortcut('Ctrl+B')
        buscaB.setStatusTip('Se busca lo seleccionado de la lista...')
        buscaB.triggered.connect(self.busca)

        limpiaB = QAction('Limpia campos', self)
        limpiaB.setShortcut('Ctrl+L')
        limpiaB.setStatusTip('Limpia campos...')
        limpiaB.triggered.connect(self.limpia)

        guardaB = QAction('Agrerga registro', self)
        guardaB.setShortcut('Ctrl+G')
        guardaB.setStatusTip('Agrergando registro...')
        guardaB.triggered.connect(self.agrega)

        self.statusBar().showMessage('Listo...')

        barraM = self.menuBar()
        ArchivoM = barraM.addMenu('&Archivo')
        ArchivoM.addAction(guardaB)
        ArchivoM.addAction(limpiaB)
        ArchivoM.addAction(buscaB)
        ArchivoM.addAction(salirB)
        
        # --------------- Campos
        # Label Fecha
        hoy = datetime.today().strftime('%Y/%m/%d')
        self.LFecha = QLabel(self)
        self.LFecha.setText(hoy)
        self.LFecha.move(1120, 25)      

        # Label Empresa
        self.L1 = QtWidgets.QLabel(self)
        self.L1.setText("Empresa:")
        self.L1.move(50,30)
        # QLineEdit Empresa
        self.T1 = QtWidgets.QLineEdit(self)
        #self.T1.setStyleSheet("QLineEdit {background-color: white; color: black; border: 0px;}")
        self.T1.setGeometry(120,30,150,30)
        self.T1.setToolTip('Escribe aqui...')
        self.T1.setPlaceholderText('Escribe aqui...')
        self.T1.setStatusTip('Escribe nombre de la empresa.')

        # Label Contacto1
        self.L2 = QtWidgets.QLabel(self)
        self.L2.setText("Contacto1:")
        self.L2.move(50,70)
        # QLineEdit Contacto1
        self.T2 = QtWidgets.QLineEdit(self)
        self.T2.setGeometry(120,70,150,30)      
        self.T2.setToolTip('Escribe aqui...')
        self.T2.setPlaceholderText('...')
        self.T2.setStatusTip('Escribe nombre del contacto.')

        # Label Contacto2
        self.L3 = QtWidgets.QLabel(self)
        self.L3.setText("Contacto2:")
        self.L3.move(50,110)
        # QLineEdit Contacto2
        self.T3 = QtWidgets.QLineEdit(self)
        self.T3.setGeometry(120,110,150,30)      
        self.T3.setToolTip('Escribe aqui...')
        self.T3.setPlaceholderText('...')
        self.T3.setStatusTip('Escribe nombre del contacto.')

        # Label Correo
        self.L4 = QtWidgets.QLabel(self)
        self.L4.setText("Correo:")
        self.L4.move(50,150)
        # QLineEdit Correo
        self.T4 = QtWidgets.QLineEdit(self)
        self.T4.setGeometry(120,150,150,30)      
        self.T4.setToolTip('Escribe aqui...')
        self.T4.setPlaceholderText('...')
        self.T4.setStatusTip('Escribe una dirección.')

        # Label Teléfono
        self.L5 = QtWidgets.QLabel(self)
        self.L5.setText("Teléfono:")
        self.L5.move(50,190)
        # QLineEdit Teléfono
        self.T5 = QtWidgets.QLineEdit(self)
        self.T5.setGeometry(120,190,150,30)      
        self.T5.setToolTip('Escribe aqui...')
        self.T5.setPlaceholderText('...')
        self.T5.setStatusTip('Escribe un teléfon.')
        self.T5.setValidator(QIntValidator())
        self.T5.setMaxLength(8)

        # Label Celular
        self.L6 = QtWidgets.QLabel(self)
        self.L6.setText("Celular:")
        self.L6.move(50,230)
        # 55 Celular
        self.Tt = QtWidgets.QLineEdit(self)
        self.Tt.setText("55")
        self.Tt.setGeometry(105,230,25,30)
        self.Tt.setEnabled(False)
        # QLineEdit Celular
        self.T6 = QtWidgets.QLineEdit(self)
        self.T6.setGeometry(130,230,150,30)      
        self.T6.setToolTip('Escribe aqui...')
        self.T6.setPlaceholderText('...')
        self.T6.setStatusTip('Escribe un celular.')
        self.T6.setValidator(QIntValidator())
        self.T6.setMaxLength(10)

        # Label Modelo
        self.L7 = QtWidgets.QLabel(self)
        self.L7.setText("Modelo:")
        self.L7.move(300,30)
        # QLineEdit Modelo
        self.T7 = QtWidgets.QLineEdit(self)
        self.T7.setGeometry(370,30,150,30)      
        self.T7.setToolTip('Escribe aqui...')
        self.T7.setPlaceholderText('...')
        self.T7.setStatusTip('Escribe el modelo.')

        # Label Serie
        self.L8 = QtWidgets.QLabel(self)
        self.L8.setText("Serie:")
        self.L8.move(600,30)
        # QLineEdit Serie
        self.T8 = QtWidgets.QLineEdit(self)
        self.T8.setGeometry(670,30,150,30)      
        self.T8.setToolTip('Escribe aqui...')
        self.T8.setPlaceholderText('...')
        self.T8.setStatusTip('Escribe la serie.')

        # Label Discos
        self.L9 = QtWidgets.QLabel(self)
        self.L9.setText("Discos:")
        self.L9.move(300,70)
        # QLineEdit Discos
        self.T9 = QtWidgets.QLineEdit(self)
        self.T9.setGeometry(370,70,150,30)      
        self.T9.setToolTip('Escribe aqui...')
        self.T9.setPlaceholderText('...')
        self.T9.setStatusTip('Tipo de discos.')

        # Label CantidadDiscos
        self.L10 = QtWidgets.QLabel(self)
        self.L10.setText("Cantidad de Discos:")
        self.L10.setGeometry(600,70,120,30)
        # QLineEdit CantidadDiscos
        self.T10 = QtWidgets.QLineEdit(self)
        self.T10.setGeometry(750,70,150,30)      
        self.T10.setToolTip('Escribe aqui...')
        self.T10.setPlaceholderText('...')
        self.T10.setStatusTip('Escribe una cantidad.')
        self.T10.setValidator(QIntValidator())

        # Label Memoria
        self.L11 = QtWidgets.QLabel(self)
        self.L11.setText("Memoria:")
        self.L11.move(300,110)
        # QLineEdit Memoria
        self.T11 = QtWidgets.QLineEdit(self)
        self.T11.setGeometry(370,110,150,30)      
        self.T11.setToolTip('Escribe aqui...')
        self.T11.setPlaceholderText('...')
        self.T11.setStatusTip('Tipo de memoria.')

        # Label CantidadMemoria
        self.L12 = QtWidgets.QLabel(self)
        self.L12.setText("Cantidad de Memoria:")
        self.L12.setGeometry(600,110,130,30)
        # QLineEdit CantidadMemoria
        self.T12 = QtWidgets.QLineEdit(self)
        self.T12.setGeometry(750,110,150,30)      
        self.T12.setToolTip('Escribe aqui...')
        self.T12.setPlaceholderText('...')
        self.T12.setStatusTip('Escribe una cantidad.')
        self.T12.setValidator(QIntValidator())

        # Label OficialSeguridad
        self.L13 = QtWidgets.QLabel(self)
        self.L13.setText("Oficial de Seguridad:")
        self.L13.setGeometry(300,180,150,30)
        # QLineEdit OficialSeguridad
        self.T13 = QtWidgets.QLineEdit(self)
        self.T13.setGeometry(450,180,150,30)      
        self.T13.setToolTip('Escribe aqui...')
        self.T13.setPlaceholderText('...')
        self.T13.setStatusTip('Escribe un usuario.')

        # Label Password
        self.L14 = QtWidgets.QLabel(self)
        self.L14.setText("Password:")
        self.L14.move(630,180)
        # QLineEdit Password
        self.T14 = QtWidgets.QLineEdit(self)
        self.T14.setGeometry(700,180,150,30)      
        self.T14.setToolTip('Escribe aqui...')
        self.T14.setPlaceholderText('...')
        self.T14.setStatusTip('Escribe el password.')

        # Label ServiceTools
        self.L15 = QtWidgets.QLabel(self)
        self.L15.setText("Service Tools:")
        self.L15.setGeometry(300,220,150,30)
        # QLineEdit ServiceTools
        self.T15 = QtWidgets.QLineEdit(self)
        self.T15.setGeometry(450,220,150,30)      
        self.T15.setToolTip('Escribe aqui...')
        self.T15.setPlaceholderText('...')
        self.T15.setStatusTip('Escribe un usuario.')

        # Label Password
        self.L16 = QtWidgets.QLabel(self)
        self.L16.setText("Password:")
        self.L16.move(630,220)
        # QLineEdit Password
        self.T16 = QtWidgets.QLineEdit(self)
        self.T16.setGeometry(700,220,150,30)      
        self.T16.setToolTip('Escribe aqui...')
        self.T16.setPlaceholderText('...')
        self.T16.setStatusTip('Escribe el password.')

        # Label Comentario
        self.L17 = QtWidgets.QLabel(self)
        self.L17.setText("Comentario:")
        self.L17.move(900,180)
        # QLineEdit Comentario
        self.T17 = QtWidgets.QLineEdit(self) # buscar un cuadro de texto mas grande
        self.T17.setGeometry(1000,180,160,80)      
        self.T17.setToolTip('Escribe aqui...')
        self.T17.setPlaceholderText('...')
        self.T17.setStatusTip('Escribe un comentario.')

        # --------------- Botones
        # PushButton Agregar
        self.BT1 = QPushButton(self)
        self.BT1.setText("Agregar")
        self.BT1.move(50,300)
        self.BT1.setStatusTip('Crearás un nuevo registro...')
        self.BT1.clicked.connect(self.agrega)

        # PushButton Limpiar
        self.BT2 = QPushButton(self)
        self.BT2.setText("Limpiar")
        self.BT2.move(170,300)
        self.BT2.setStatusTip('Borraras lo escrito...')
        self.BT2.clicked.connect(self.limpia)

        # PushButton Eliminar
        self.BT4 = QPushButton(self)
        self.BT4.setText("Eliminar")
        self.BT4.move(290, 300)
        self.BT4.setStatusTip('Elimina...')
        self.BT4.clicked.connect(self.elimino)
        
        # PushButton Actualizar
        self.BT5 = QPushButton(self)
        self.BT5.setText("Actualizar")
        self.BT5.move(410, 300)
        self.BT5.setStatusTip('Actualiza...')
        self.BT5.clicked.connect(self.actualizo)

        # PushButton Salir
        self.BT6 = QPushButton(self)
        self.BT6.setText("Salir")
        self.BT6.move(530, 300)
        self.BT6.setStatusTip('ADIOS, Cerraras el programa.')
        self.BT6.clicked.connect(self.salida)

        # PushButton Buscar
        self.BT3 = QPushButton(self)
        self.BT3.setText("Buscar")
        self.BT3.move(780, 300)
        self.BT3.setStatusTip('Buscar...')
        self.BT3.clicked.connect(self.busca)
        
        # ComboBox
        self.CB = QComboBox(self)
        self.CB.move(900, 300)
        self.TxtCB()

        # x, y, Ancho, altura
        self.setGeometry(100, 100, 1200, 400)
        self.setWindowTitle('Agenda')
        self.show()

    # --------------- Funciones
    # Funcion Limpia
    def limpia(self):
        self.T1.clear(),  self.T2.clear(),  self.T3.clear(),  self.T4.clear(),  self.T5.clear(),  self.T6.clear(),  self.T7.clear()
        self.T8.clear(),  self.T9.clear(),  self.T10.clear(), self.T11.clear(), self.T12.clear(), self.T13.clear(), self.T14.clear()
        self.T15.clear(), self.T16.clear(), self.T17.clear()
        self.habilita()
    # Funcion Habilita
    def habilita(self):
        self.T1.setEnabled(True), self.T2.setEnabled(True), self.T3.setEnabled(True), self.T4.setEnabled(True)
        self.T5.setEnabled(True), self.T6.setEnabled(True), self.T7.setEnabled(True), self.T8.setEnabled(True)
        self.T9.setEnabled(True), self.T10.setEnabled(True), self.T11.setEnabled(True), self.T12.setEnabled(True)
        self.T13.setEnabled(True), self.T14.setEnabled(True), self.T15.setEnabled(True), self.T16.setEnabled(True)
        self.T17.setEnabled(True)
    # Funcion Bloqueo
    def bloqueo(self):
        self.T1.setEnabled(False), self.T2.setEnabled(False), self.T3.setEnabled(False), self.T4.setEnabled(False)
        self.T5.setEnabled(False), self.T6.setEnabled(False), self.T7.setEnabled(False), self.T8.setEnabled(False)
        self.T9.setEnabled(False), self.T10.setEnabled(False), self.T11.setEnabled(False), self.T12.setEnabled(False)
        self.T13.setEnabled(False), self.T14.setEnabled(False), self.T15.setEnabled(False), self.T16.setEnabled(False)
        self.T17.setEnabled(False)
    # Funcion salida
    def salida(self):
        msg = QMessageBox.question(self,'¿Seguro...?',"¿Seguro quieres salir?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if msg == QMessageBox.Yes:
            self.sal()
    # Funcion TxtCB
    def TxtCB(self):
        self.CB.clear()
        bd = ayudante("pgm.db")
        busqueda = bd.select("SELECT Empresa FROM Contactos")
        for x in busqueda:
            self.CB.addItems(x)
    # Funcion Busca
    def busca(self):
        self.limpia()
        db = ayudante("pgm.db")
        e = [self.CB.currentText()]
        busca = db.editar("SELECT * FROM Contactos WHERE Empresa = ?", e )
        for x in busca:
            self.T1.setText(x[1])
            self.T2.setText(x[2])
            self.T3.setText(x[3])
            self.T4.setText(x[4])
            self.T5.setText(str(x[5]))
            self.T6.setText(str(x[6]))
            self.T7.setText(x[7])
            self.T8.setText(x[8])
            self.T9.setText(x[9])
            self.T10.setText(str(x[10]))
            self.T11.setText(x[11])
            self.T12.setText(str(x[12]))
            self.T13.setText(x[13])
            self.T14.setText(x[14])
            self.T15.setText(x[15])
            self.T16.setText(x[16])
            self.T17.setText(x[17])
    # Funcion Actualizo
    def actualizo(self):
        if self.textos():
            a = self.textosActualizados()
            db = ayudante("pgm.db")
            valores  = a
            agregar = db.editar("""UPDATE Contactos SET Contacto1 = ?,
                                                        Contacto2 = ?,
                                                        Correo = ?,
                                                        Telefono = ?,
                                                        Celular = ?,
                                                        Modelo = ?,
                                                        Serie = ?,
                                                        Discos = ?,
                                                        CantidadD = ?,
                                                        Memoria = ?,
                                                        CantidadM = ?,
                                                        OficialS = ?,
                                                        PassOficialS = ?,
                                                        ServiceT = ?,
                                                        PassServiceT = ?,
                                                        Comentario = ?,
                                                        Estatus = ? 
                                                        WHERE Empresa = ?""", valores)
            msg = QMessageBox.about(self,'Algo pasa...', "Se modifico correctamente.")
        else:
            msg2 = QMessageBox.warning(self,'Algo pasa...', "No se pudo agregar nada.")
    # Funcion Textos
    def textos(self):
        if len(self.T1.text()) != 0 and len(self.T2.text()) != 0:
            T1 = self.T1.text()
            T2 = self.T2.text()
            T3 = self.T3.text()
        else:
            msg = QMessageBox.warning(self,'Algo pasa...', "Falta texto, puede ser en Empresa o Contacto1.")
        if len(self.T4.text()) != 0 and len(self.T5.text()) != 0:
            T4  = self.T4.text()
            T5  = self.T5.text()
        else:
            msg = QMessageBox.warning(self,'Algo pasa...', "Falta texto, puede ser en Correo o Teléfono.")
        T6  = self.Tt.text() + self.T6.text() 
        T7  = self.T7.text()
        T8  = self.T8.text()
        T9  = self.T9.text()
        T10 = self.T10.text()
        T11 = self.T11.text()
        T12 = self.T12.text()
        T13 = self.T13.text()
        T14 = self.T14.text()
        T15 = self.T15.text()
        T16 = self.T16.text()
        T17 = self.T17.text()
        return T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,1
    # Funcion TextosActualizados
    def textosActualizados(self):
        if len(self.T1.text()) != 0 and len(self.T2.text()) != 0:
            T1 = self.T1.text()
            T2 = self.T2.text()
            T3 = self.T3.text()
        else:
            msg = QMessageBox.warning(self,'Algo pasa...', "Falta texto, puede ser en Empresa o Contacto1.")
        if len(self.T4.text()) != 0 and len(self.T5.text()) != 0:
            T4  = self.T4.text()
            T5  = self.T5.text()
        else:
            msg = QMessageBox.warning(self,'Algo pasa...', "Falta texto, puede ser en Correo o Teléfono.")
        T6  = self.Tt.text() + self.T6.text() 
        T7  = self.T7.text()
        T8  = self.T8.text()
        T9  = self.T9.text()
        T10 = self.T10.text()
        T11 = self.T11.text()
        T12 = self.T12.text()
        T13 = self.T13.text()
        T14 = self.T14.text()
        T15 = self.T15.text()
        T16 = self.T16.text()
        T17 = self.T17.text()
        return T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14,T15,T16,T17,3,T1
    # Funcion agrega
    def agrega(self):
        if self.textos():
            self.bloqueo()
            db = ayudante("pgm.db")
            valores  = self.textos()
            agregar = db.editar("INSERT INTO Contactos VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", valores)
            msg = QMessageBox.about(self,'Algo pasa...', "Se agrego correctamente.")
            self.TxtCB()
        else:
            msg2 = QMessageBox.warning(self,'Algo pasa...', "No se pudo agregar nada.")
    # Funcion Elimino
    def elimino(self):
        msg = QMessageBox.question(self,'¿Seguro...?',"¿Seguro quieres eliminar esto...?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if msg == QMessageBox.Yes:
            if self.textos():
                db = ayudante("pgm.db")
                a = self.T1.text()
                valores  = [a]
                agregar = db.editar("DELETE FROM Contactos WHERE Empresa = ?", valores)
                self.limpia()
                self.TxtCB()
                msg1 = QMessageBox.about(self,'Algo pasa...', "Se elimino correctamente.")
            else:
                msg2 = QMessageBox.warning(self,'Algo pasa...', "No se pudo eliminar nada.")


# Inicio
if __name__ == '__main__':
    app = QApplication(sys.argv)
    vtn = vtnAgrergar()
    sys.exit(app.exec_())
