import cv2
import numpy as np
from tensorflow.python.keras.models import load_model
from fastapi import FastAPI, UploadFile, File
import matplotlib.pyplot as plt
import aiofiles as aiofiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    PredecirFrontParametro('Test_images/1/As_de_bastos-1.jpg')
    return {"Hello": "World"}


@app.post("/upload-file/")
async def create_upload_file(uploaded_file: UploadFile = File(...)):
    file_location = f"/ProyectoInteligentes2/ProyectoFinalInteligentes2\Codigo/{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())

    valor,nombre = PredecirFrontParametro(uploaded_file.filename)
    return {"porcentaje": f"{valor}", 
            "Carta": f"{nombre}"}


categorias = ['As_de_bastos', 'As_de_copas', 'As_de_espadas', 'As_de_oros',
              'Caballo_de_bastos', 'Caballo_de_copas', 'Caballo_de_espadas', 'Caballo_de_oros',
              'Cinco_de_bastos', 'Cinco_de_copas', 'Cinco_de_espadas', 'Cinco_de_oros',
              'Cuatro_de_bastos', 'Cuatro_de_copas', 'Cuatro_de_espadas', 'Cuatro_de_oros',
              'Dos_de_bastos', 'Dos_de_copas', 'Dos_de_espadas', 'Dos_de_oros',
              'Rey_de_bastos', 'Rey_de_copas', 'Rey_de_espadas', 'Rey_de_oros',
              'Seis_de_bastos', 'Seis_de_copas', 'Seis_de_espadas', 'Seis_de_oros',
              'Siete_de_bastos', 'Siete_de_copas', 'Siete_de_espadas', 'Siete_de_oros',
              'Sota_de_bastos', 'Sota_de_copas', 'Sota_de_espadas', 'Sota_de_oros',
              'Tres_de_bastos', 'Tres_de_copas', 'Tres_de_espadas', 'Tres_de_oros']


class prediccion():
    """
    Carga el modelo de la red neuronal de la ruta especificada
    """
    maxvalue = 0


    def __init__(self):
        self.rutaModelo = "modeloReconocimientoBarajaEsp.keras"
        self.model = load_model(self.rutaModelo)
        self.width = 128
        self.heigth = 128

    def predecir(self, imagen):
        """
            Toma la imagen de entrada y realiza el proceso de predicci??n
        """
        imagen = cv2.resize(imagen, (self.width, self.heigth))
        imagen = imagen.flatten()
        imagen = np.array(imagen)
        imagenNormalizada = imagen/255
        pruebas = []
        pruebas.append(imagenNormalizada)
        imagenesAPredecir = np.array(pruebas)
        predicciones = self.model.predict(x=imagenesAPredecir)
        claseMayorValor = np.argmax(predicciones, axis=1)
        self.maxvalue = np.max(predicciones)
        print('Valor maximo' , self.maxvalue)
        print('Predicciones', predicciones)
        print(claseMayorValor)
        return claseMayorValor[0]

def PredecirFrontParametro(imagen):
    reconocimiento = prediccion()
    imagenPrueba = cv2.imread(
        imagen, 0)
    # print(imagenPrueba)
    indiceCategoria = reconocimiento.predecir(imagenPrueba)
    print("La imagen cargada es ", categorias[indiceCategoria])

    imagen = cv2.imread(
        imagen, 0)

    if imagen is None:
        print('error al cargar la imagen')
    cv2.destroyAllWindows()
    return reconocimiento.maxvalue, categorias[indiceCategoria]
