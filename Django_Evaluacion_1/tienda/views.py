from django.shortcuts import render

def index (request):
    return render(request, 'web\index.html')

def mause(request):
    data = {
        "titulo": "Mauses Opticos",
        "producto1": {
            "nombre": "Logitech G203",
            "foto": "mause1.png",
            "descripcion": "Con una velocidad de transmisión de 1 ms, el G203 es 8 veces más rápido que el mouse estándar, lo que hace que la respuesta en pantalla sea prácticamente instantánea. Ligero, duradero y cómodo, G203 también cuenta con sensor HERO y LIGHTSYNC RGB."
        },
        "producto2": {
            "nombre": "Logitech G502 Hero",
            "foto": "mause2.png",
            "descripcion": "Diseñado para un desempeño avanzado en los juegos. G502 HERO cuenta con un sensor de juegos HERO 25K con seguimiento de precisión submicrométrica, LIGHTSYNC RGB personalizable, perfiles integrados, pesos reposicionables y mucho más."
        },
        "producto3": {
            "nombre": "Logitech G Pro",
            "foto": "mause3.png",
            "descripcion": "El mouse para juegos PRO Gaming Mouse se creó con un objetivo: ayudarte a triunfar en el entorno extremadamente competitivo y acelerado de los deportes electrónicos. Se ha optimizado con sensor HERO para darle la portentosa velocidad y precisión necesarias para ganar."
        }
    }
    return render(request, 'web/producto.html', data)

def teclado(request):
    data = {
        "titulo": "Teclados Mecanicos",
        "producto1": {
            "nombre": "Logitech G513 Carbon",
            "foto": "teclado1.png",
            "descripcion": "Teclado para juegos avanzados con interruptores mecánicos GX a elegir. El reposamanos extraíble de espuma viscoelástica y la construcción de aleación de aluminio premium complementan las características de G513 para hacerlo el mejor de su clase."
        },
        "producto2": {
            "nombre": "Logitech G Pro x",
            "foto": "teclado2.png",
            "descripcion": "Diseño PRO de eficacia probada en torneos, ahora con interruptores mecánicos GX profesionales intercambiables a elegir: con clic perceptible, táctiles y lineales. Hecho para ganar, con la colaboración de los mejores deportistas de esports del mundo."
        },
        "producto3": {
            "nombre": "logitech G915 tkl",
            "foto": "teclado3.png",
            "descripcion": "Un gran avance en diseño e ingeniería, ahora en combinaciones de colores en blanco y negro. G915 TKL incorpora tecnología inalámbrica LIGHTSPEED de calidad profesional, RGB LIGHTSYNC avanzada e interruptores mecánicos de perfil bajo y alto desempeño. Creado meticulosamente con materiales premium, el G915 TKL tiene un sofisticado diseño de incomparable belleza, resistencia y desempeño. Y ahora con un diseño aún más compacto. G915 TKL. Juega en la siguiente dimensión."
        }
    }
    return render(request, 'web/producto.html', data)

def casco(request):
    data = {
        "titulo": "Cascos",
        "producto1": {
            "nombre": "Logitech G733 Lightspeed",
            "foto": "casco1.png",
            "descripcion": "Audífonos inalámbricos con micrófono para juegos diseñados para desempeño y confort. Equipados con todo el sonido envolvente, los filtros de voz y la iluminación avanzada que necesitas para lucir, sonar y jugar con más estilo que nunca."
        },
        "producto2": {
            "nombre": "logitech G533",
            "foto": "casco2.png",
            "descripcion": "G533 refleja con precisión el entorno de juego con sonido envolvente virtual de 7.1 canales. Oye y detecta enemigos, amenazas y todo lo que te rodea. Usa Logitech G HUB para ajustar los niveles de volumen de cada uno de los 7 canales de audio. Por ejemplo, puedes amplificar sonidos de juego procedentes de canales posteriores, para oír cosas que ocurren a tu espalda."
        },
        "producto3": {
            "nombre": "logitech G PRO X 2 LIGHTSPEED",
            "foto": "casco3.png",
            "descripcion": "Diseñados con los profesionales. Concebidos para ganar. Los audífonos con micrófono PRO X 2 LIGHTSPEED ofrecen sonido profesional, tecnología inalámbrica LIGHTSPEED y confort superior para alcanzar los más altos niveles de competencia. Oye cada paso, acción y tiro de anilla de granada con el inmersivo espacio sonoro que posibilitan los transductores de grafeno."
        }
    }
    return render(request, 'web/producto.html', data)