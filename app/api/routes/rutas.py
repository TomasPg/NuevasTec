from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.DTO import UsuarioDTOPeticion, UsuarioDTORespuesta
from app.api.models.modelosApp import Usuario
from app.api.schemas.DTO import GastoDTOPeticion, GastoDTORespuesta
from app.api.models.modelosApp import Gasto
from app.api.schemas.DTO import CategoriaDTOPeticion, CategoriaDTORespuesta
from app.api.models.modelosApp import Categoria
from app.api.schemas.DTO import MetodoPagoDTOPeticion, MetodoPagoDTORespuesta
from app.api.models.modelosApp import MetodoPago
from app.database.configuration import sessionLocal, engine

#Para que un api funcione debe tener un archivo enrutador
rutas=APIRouter() #ENDPOINTS
#Crear una funcion para establecer cuando yo quiera y necesite

#conexion hacia la base de datos
def getDataBase():
    basedatos=sessionLocal()
    try:
        yield basedatos
    except Exception as error:
        basedatos.rollback()
        raise error
    finally:
        basedatos.close()
#PROGRAMACION DE CADA UNO DE LOS SERVICIOS
#QUE OFRECERA NUESTRA API

#SERVICIO PARA REGISTRAR O GUARDAR UN USUARIO EN BD

#Ususarios
@rutas.post("/Usuarios", response_model = UsuarioDTORespuesta)
def guardarUsuario(datosPeticion: UsuarioDTOPeticion, db: Session = Depends(getDataBase)):

    try:
        usuario = Usuario(
            nombres = datosPeticion.nombre,
            edad = datosPeticion.edad,
            telefono = datosPeticion.telefono,
            correo = datosPeticion.correo,
            contraseña = datosPeticion.contraseña,
            fechaRegistro = datosPeticion.fechaRegistro,
            ciudad = datosPeticion.ciudad
        )

        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return UsuarioDTORespuesta(
            id=Usuario.id,
            nombre=Usuario.nombres,
            telefono=Usuario.telefono,
            ciudad=Usuario.ciudad,
            edad=Usuario.edad
        )
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code = 400, detail = f'Eror al Registrar el Usuario {error}')

@rutas.get('/Usuarios', response_model = List[UsuarioDTORespuesta]) 
def buscarUsuarios(db: Session = Depends(getDataBase)):

    try:
        listadoDeUsuarios = db.query(Usuario).all()
        return [
            UsuarioDTORespuesta(
                id=Usuario.id,
                nombre=Usuario.nombres,
                telefono=Usuario.telefono,
                ciudad=Usuario.ciudad
            ) for Usuario in listadoDeUsuarios
        ]

    except Exception as error:
        db.rollback()
        raise HTTPException(status_code = 400, detail = f'Eror al Registrar el Usuario {error}')
    
#Gastos -----------------------------------------------------------------------------------------------------
@rutas.post("/Gastos", response_model = GastoDTORespuesta)
def guardarUsuario(datosPeticion: GastoDTOPeticion, db:Session = Depends(getDataBase)):

    try:
        gasto = Gasto(
            monto = datosPeticion.monto,
            fecha = datosPeticion.fecha,
            descripcion = datosPeticion.descripcion,
            nombre = datosPeticion.nombre
        )

        db.add(gasto)
        db.commit()
        db.refresh(gasto)
        return GastoDTORespuesta(
            id=Gasto.id,
            monto=Gasto.monto,
            fecha=Gasto.fecha,
            descripcion=Gasto.descripcion,
            nombre=Gasto.nombre
        )
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code = 400, detail = f'Eror al Registrar el Usuario {error}')
    
@rutas.get('/Gastos', response_model = List[GastoDTORespuesta]) 
def buscarGastos(db: Session = Depends(getDataBase)):

    try:
        listadoDeGastos = db.query(Gasto).all()
        return [
            GastoDTORespuesta(
                id=Gasto.id,
                monto=Gasto.monto,
                fecha=Gasto.fecha,
                descripcion=Gasto.descripcion,
                nombre=Gasto.nombre
            ) for Gasto in listadoDeGastos
        ]

    except Exception as error:
        db.rollback()
        raise HTTPException(status_code = 400, detail = f'Eror al Registrar el Usuario {error}')

#Categoria -----------------------------------------------------------------------------------------------------
@rutas.post("/Categorias", response_model = CategoriaDTORespuesta)
def guardarUsuario(datosPeticion: CategoriaDTOPeticion, db:Session = Depends(getDataBase)):

    try:
        categoria = Categoria(
            nombreCategoria = datosPeticion.nombreCategoria,
            descripcion = datosPeticion.descripcion
        )

        db.add(categoria)
        db.commit()
        db.refresh(categoria)
        return CategoriaDTORespuesta(
            id=Categoria.id,
            nombreCategoria=Categoria.nombreCategoria,
            descripcion=Categoria.descripcion
        )
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code = 400, detail = f'Eror al Registrar el Usuario {error}')
    
@rutas.get('/Categorias', response_model = List[CategoriaDTORespuesta]) 
def buscarCategorias(db: Session = Depends(getDataBase)):

    try:
        listadoDeCategorias = db.query(Categoria).all()
        return [
            CategoriaDTORespuesta(
                id=Categoria.id,
                nombreCategoria=Categoria.nombreCategoria,
                descripcion=Categoria.descripcion
            ) for Categoria in listadoDeCategorias
        ]

    except Exception as error:
        db.rollback()
        raise HTTPException(status_code = 400, detail = f'Eror al Registrar el Usuario {error}')

#Metodo Pago -----------------------------------------------------------------------------------------------------
@rutas.post("/Metodospago")
def guardarUsuario(datosPeticion: MetodoPagoDTOPeticion, db:Session = Depends(getDataBase)):

    try:
        metodoPago = MetodoPago(
            nombreMetodo = datosPeticion.nombreMetodo,
            descripcion = datosPeticion.descripcion
        )

        db.add(metodoPago)
        db.commit()
        db.refresh(metodoPago)
        return metodoPago
    except Exception as error:
        db.rollback()
        raise HTTPException(status_code = 400, detail = f'Eror al Registrar el Usuario {error}')
    
@rutas.get('/Metodospago', response_model = List[MetodoPagoDTORespuesta]) 
def buscarMetodosPago(db: Session = Depends(getDataBase)):

    try:
        listadoDeMetodosPago = db.query(MetodoPago).all()
        return listadoDeMetodosPago

    except Exception as error:
        db.rollback()
        raise HTTPException(status_code = 400, detail = f'Eror al Registrar el Usuario {error}')