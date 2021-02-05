# Importamos el módulo
import sqlite3

conexion = sqlite3.connect('database.db')
cursor = conexion.cursor()

#----------------Eliminar tablas si existen
cursor.execute("DROP TABLE IF EXISTS questions;")
cursor.execute("DROP TABLE IF EXISTS answers;")

#-----------------Crear Tablas-------------------
cursor.execute("CREATE TABLE questions (\
id_pregunta     INTEGER        PRIMARY KEY    AUTOINCREMENT,\
pregunta     VARCHAR(120)    UNIQUE,\
id_respuesta    INTEGER \
);")

cursor.execute("CREATE TABLE answers (\
id_respuesta     INTEGER        PRIMARY KEY    AUTOINCREMENT,\
respuesta     VARCHAR(120),\
id_pregunta INTEGER);")


#-----------------Crear Registros----------------
dataQuestions = [
		(1, "¿Una empresa que se dedica a la distribución de huevos en Bogotá, visualiza que su negocio está   creciendo de forma exponencial porque sus pedidos crecen cada vez más, se requiere tener más poder  de distribución pero al acercarse a sus competidores para ofrecer alianzas, se da cuenta que no quieren ningun tipo de alianza, ahora usted como experto en estrategias que sugiere que se deberia hacer?", 2),
		(2, "Colombina decide sacar al mercado un producto unico en Colombia, el cúal por su exclusividad en el mercado deciden cobrar 5.000 pesos la unidad, a pesar del precio es único y por eso se vende muy bien. En base a lo anterior escoge la estrategia adoptada por Colombina?", 5),
		(3, "¿Cocacola es una multinacional que se encuentra en lo más alto de las empresas que venden gaseosa, es un intento casi imposible para las demas compañias que fabrican gaseosas subir para llegar    hasta donde se encuentra. El anterior enunciado se puede asociar a?", 8),
		(4, "¿la notación n=2, Juego G={J,S,U}, Jugadores J={ETIC1, ETIC2}, Estrategias S1={Acectar, No Aceptar}, S2={Acectar, No Aceptar}, es la representación de un juego en forma normal. Seria correcto     decir que?", 11),
		(5, "Bavaria decide crear varios productos nuevos, también emprende un proyecto de compra de algunos   distribuidores para montar sus propias casetas de venta. Lo anterior se podria asociar a que grupo de estrategias", 13),
		(6, "¿De la matriz de pagos podemos concluir que?", 16),
		(7, "¿en la siguiente matriz de pagos, si Comestibles Aldor promociona solamente Pinpop Bumba,         Colombina aplica la estrategia mixta (1/2, 1/2, 0). Cual seria el resultado en ganancias?", 18),
		(8, "¿Parmalat tomó la decisión de crear un nuevo postre, que estrategia deberia emplear para impulzar en el mercado el nuevo producto?", 24),
		(9, "¿Renault decide sacar una linea de temporal muy atractiva llamada 'Logan light max', impulza la   seria por redes sociales, televisión y varios medios de comunicación más, la linea tiene la       condición es que tiene pocas unidades, se vendera rápido y las ganancias llegaran en un tiempo    muy corto. A que estrategia militar se podria asociar?", 25),
		(10, "¿en la siguiente matriz de pagos escoja que estrategia es la mejor para la empresa Pepsico?", 28),
		(11, "¿Se abre una licitación para proveer energía electrica en el caribe, puesto que Electricaribe se  va, Entonces las empresas Caribesol y Caribeluna se reparten la conceción por la mitad, y asi las ganancias seran por iguales para cada empresa. De lo anterior se podria decir que?", 30),
		(12, "¿Cuanto es la ganancia de Bavaria promocionando Poker si Central cervecera promociona Heineken?",34),
		(13, "¿cuando los ejercitos robaban, quemaban o atacaban los recursos del enemigo. Cómo se le conoce a  está estrategia?", 38),
		(14, "¿las caracteristicas: completamente determinista y no involucra azar. Son juegos de?", 40),
		(15, "¿cuando se introducia un caballo de troya o espias en el ejercito enemigo se conoce cómo?", 43),
		(16, "¿una de las caracteristicas del equilibrio de nash es?", 48),
		(17, "¿una empresa que distribuye huevos quiere emprender un proyecto que consiste en adquirir un galpón que tipo de estrategia estaria adoptando?", 53),
		(18, "¿el liderazgo en costes se basa en vender los productos o servicios a un precio inferior al de la competencia. A que estrategia pertenece?", 54),
		(19, "¿cual seria la descripción para pinta en estrategias militares?", 60)
		]

dataAnswers = [
			(1, "Comprar alguna empresa de la competencia para ganar nueva fuerza que apoye a su empresa.", 1),
			(2, "Realizar alianzas con empresas de transporte tercerizada para asi atender la demanda del momento.", 1),
			(3, "Comprar 2 camiones más para tener más capacidad de entrega los nuevos pedidos.", 1),
			(4, "Penetración del mercado.", 2),
			(5, "Estrategia de diferenciación.", 2),
			(6, "Estrategia del enfoque.", 2),
			(7, "Pinta.", 3),
			(8, "Terreno Elevado.", 3),
			(9, "Es un Juego con 1 jugador, 4 estrategias", 4),
			(10, "Es un Juego con 2 jugadores, 2 estrategias.", 4),
			(11, "Es un Juego con 2 jugadores, 4 estrategias", 4),
			(12, "Ninguna de las anteriores.", 4),
			(13, "Diversificación, integración o segmentación.", 5),
			(14, "Guerra relampago, pinta o combates de guerrilla.", 5),
			(15, "Equilibrio de nash o el dilema de los prisioneros.", 5),
			(16, "Siempre proporciona una mayor utilidad a alguno de las dos empresas independiente de la estrategia elegida del otro jugador.", 6),
			(17, "Proporsiona al menos la misma utilidad para todas las estrategias independiente de la estrategia elegida del otro jugador.", 6),
			(18, "2 Billones.", 7),
			(19, "3 Billones.", 7),
			(20, "5 Billones.", 7),
			(21, "Ninguna de las anteriores.", 7),
 			(22, "Penetración del mercado.", 8),
 			(23, "Segmentación del mercado.", 8),
 			(24, "Diversificación horizontal.", 8),
			(25, "Es una ataque rápido y decisivo.", 9),
			(26, "Consiste en atacar los recursos del enemigo.", 9),
			(27, "Distracción en el centro para que allí valla el ejercito enemigo.", 9),
			(28, "Promocionar más papas Margarita", 10),
			(29, "Promocionar más Chitos Cheetos", 10),
			(30, "Que hubo un óptimo de Pareto.", 11),
			(31, "Que hubo un equilibrio de Nash.", 11),
			(32, "Ninguna de las anteriores.", 11),
			(33, "7 Billones.", 12),
			(34, "14 Billones.", 12),
			(35, "15 Billones.", 12),
			(36, "Flancos.", 13),
			(37, "Terreno elevado.", 13),
			(38, "Negación de recursos.", 13),
			(39, "Infiltración.", 13),
			(40, "Estrategia pura.", 14),
			(41, "Estrategia mixta.", 14),
			(42, "Negación de recursos.", 15),
			(43, "Infiltración.", 15),
			(44, "Combate de guerrilla.", 15),
			(45, "Ninguna de las anteriores.", 15),
			(46, "El juego es infinito.", 16),
			(47, "Es una distribución de probabilidad sobre estrategias puras.", 16),
			(48, "Cada jugador conoce y ha adoptado su mejor estrategia, y todos conocen las estrategias de los otros.", 16),
			(49, "Ninguna de las anteriores.", 16),
 			(50, "Diversificación concentrica.", 17),
 			(51, "Penetración del mercado.", 17),
 			(52, "Integración Horizontal.", 17),
 			(53, "Integración Vertical hacia atras.", 17),
			(54, "Porter, Liderazgo en costes.", 18),
			(55, "Porter, Estrategias puras.", 18),
			(56, "Nash, Liderazgo en costes.", 18),
			(57, "Porter, Estrategia del enfoque.", 18),
			(58, "Consiste en atacar los recursos del enemigo.", 19),
			(59, "Distracción en el centro para que allí valla el ejercito enemigo.", 19),
			(60, "Hacer creer una estrategia mientras se tiene otra.", 19),
			(61, "Ninguna de las anteriores.", 19)
			]

cursor.executemany("INSERT INTO questions VALUES (?,?,?)", dataQuestions)
cursor.executemany("INSERT INTO answers VALUES (?,?,?)", dataAnswers)
conexion.commit()
conexion.close()