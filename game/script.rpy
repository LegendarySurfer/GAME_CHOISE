#definimos los personajes
define jugador = Character("Adam",color="#1AD1EA")   
define ser = Character("Juego",color="#EA2A1A") 
define hermana = Character("Sara",color="#FF00D4")
define perro = Character("Cerbero",color="#C76E19")

#Comienza el programa
label start:
    
    #Aplicamos el fondo
    scene fondo1

    #Ponemos musica
    play music "audio/relax.mp3"

    "Te despiertas por el agobiante calor de verano, mientras mirabas el techo, te apetece:"
    
    #Primer menu de elecciones
    menu: 
        "Jugar a la consola que tienes en el salón":
            jump respuesta1 #completado
        "Ir a la nevera para comer algo":  
            jump respuesta2 #completado
        "Ir a pasear a tu perro":
            jump respuesta3   


#Escena de la primera eleccion
label respuesta1:
    
    "Te incorporas para jugar y miras los diferentes juegos que hay:"
    menu: 
        "Calculo Math":
            jump respuesta1_1 #completado
        "Guess the answer":
            jump respuesta1_2 #completado

label respuesta1_1:    
    "Enciendes la tele y la consola y empiezas a jugar, el juego trata sobre retos matemáticos."
    "¿Podrás superarlos?"
    "Cuanto es 100-50+200-15+(100-50):"
    menu:
        "La respuesta es 285":
            jump respuesta1_3 #completado
        "La respuesta es 305":    
            jump respuesta1_4 #completado

label respuesta1_3:
    "¡¡Has acertado!!Ahora se complicara un poco más¿preparado?"
    "Cuanto es (100-35)+(50-45)+200:"
    menu:
        "La respuesta es 270":
            jump respuesta1_5 #completado
        "La respuesta es 280":
            jump respuesta1_6 #completado
            
label respuesta1_4:
    
    "Has fallado, después de este difícil reto te das cuenta que 
    tu perro te lleva ladrando un rato y te preparas para sacarlo a pasear."
    jump finalPrologo
    
label respuesta1_5: 
    "¡¡Has vuelto a acertar!!" 

    "Después de estar un poco más jugando no te apetece seguir jugando y decides sacar a pasear a tu perro
    ya que lleva un rato ladrándote para que lo saques a pasear."
    jump finalPrologo

label respuesta1_6:
    "La respuesta es incorrecta, te cansas de este juego y vas a pesear a tu perro. "
    jump finalPrologo

label respuesta1_2:   
    "Enciendes la tele , la consola y empiezas a jugar, el juego trata sobre retos"
    "¿Podrás superarlos?"
    "Vamos con tu primer reto: ¿Cómo se llama el creador de este juego?:"
    show hermano at left
    jugador"¿Juego?"
    hide hermano
    menu:
        "LS":
            jump respuesta1_7 #completado
        "PS":
            jump respuesta1_8 #completado

label respuesta1_7:
    "¡¡Has acertado!! Pasamos a la siguiente ronda."
    "¿Qué estabas haciendo antes de empezar a jugar a este juego?"
    show hermano at left
    jugador "¿Cómo sabe lo que estaba haciendo?"
    hide hermano

    menu:
        "Mirar el techo":
            jump respuesta1_9 #completado
        "Ver la tele":
            jump respuesta1_10 #completado

label respuesta1_8:    
    "Has fallado."
    show hermano at left
    jugador "Que clase de juego es este, mejor voy a pasear a mi perro antes de que sea mas tarde."
    hide hermano
    jump finalPrologo

label respuesta1_9:
    "¡¡Has acertado!!"
    show hermano at left
    jugador "¿Cómo sabia el juego todo esto?"
    hide hermano
    "Decides irte a sacar a pasear a tu perro antes de que sea muy tarde."
    jump finalPrologo

label respuesta1_10:    
    "Has fallado, te incomoda la pregunta así que  prefieres sacar a pasear a tu perro antes de que sea tarde."
    jump finalPrologo

#Final prologo
label finalPrologo:

    scene fondo3 with fade
    stop music
    play music "audio/intro.ogg"
    "Sales por la puerta con tu perro,todo va bien, lo llevas al parque de siempre.
    Para que no sea tan aburrido llamas a tu amigo para dar un paseo por el parque con el."

    "Después de un rato de estar en el parque hablando os vais cada uno a su casa, cómo los 
    dos vivís lejos del uno y ya es casi de noches te diriges rápido a casa no sea que pase  ∞ ╰╮❪ ❫ 
    como habías escuchado en las noticias. "

    "Justo antes de llegar a casa se pone el semáforo en rojo y tienes que esperar,
    al lado tuyo divisas a una persona, no logras verle la cara porque va muy tapado 
    pero ves que va a cruzar la acera,"
    " para impedir un accidente corres a detenerlo pero antes de agarrarlo miras a ver 
    si viene algún vehículo pero ya es tarde, solo ves dos rayos de luz dirigiéndose a ti muy rápido."
    
    "Sin pensarlo dos veces cierras los ojos, dé repente todo estaba tranquilo, 
    lo único que sientes es como si tu cuerpo flotara en el espacio, todo estaba en 
    silencio, no sabes lo que pasa, abres los ojos y no crees lo que ves delante tuyo."
    return 
#-----------------------------------------------------------------------------

#Escena de la segunda eleccion
label respuesta2:
    #salon con nevera
    scene fondo2 with fade
    "Te levantas del sofá, cuando estás a punto de ver que hay en la nevera tu perro ladra para que lo lleves a pasear."    
    menu:
        "Ignorarlo":
            jump respuesta2_1 #completado
        "Te preparas para ir a pasearlo. Cuando ya estas listo vas con tu perro a la puerta para pasearlo": 
            jump respuesta2_1 #completado

label respuesta2_1:
    "No le haces caso a tu perro."
    show hermana at right
    hermana "Porque esta tan alterado Cerbero."
    show hermano at left
    jugador "No se, no le hago nada."
    hermana "¿No le has sacado a pasear?"
    jugador "No, no me apetece."
    hermana "Pues sacalo ahora mismo"
    perro "Guau"
    hide hermano 
    hide hermana
    jump finalPrologo

label respuesta2_2:    
    "Te preparas para ir a pasear a Cerbero.
    Cuando ya estas listo vas a la puerta para pasearlo." 
    jump finalPrologo   

#-----------------------------------------------------------------------------
#Escena de la tercera eleccion
label respuesta3:
    #abitacion con hermana
    "Estas a punto de pasear a Cerbero pero en verdad te dan ganas de jugar a la consola del salón,
    piensas que puede sacarlo tu hermana."
    menu:
        "Prepararse para ira a pasear a Cerbero de todas formas":
            jump finalPrologo #completado
        "Preguntarle a tu hermana":    
            jump respuesta3_1 #completado

label respuesta3_1:
    scene fondo4 with fade
    "Subes para ir a la habitación de tu hermana, parece que esta jugando a un juego
    de fantasía en el ordenador, aunque según viste en las noticias parece que da 
    algún tipo de ∞ ╰╮❪ ❫ en algunas personas."
    menu:
        "No la molestas y vas a sacar a Cerbero":
            jump finalPrologo #completado
        "Preguntas a tu hermana si puede sacar a Cerbero":          
            jump respuesta3_2 #completado

label respuesta3_2:
    show hermana at right
    hermana "Ahora no puedo sacar a pasear a Cerbero, sacalo tu."
    show hermano at left
    jugador "No, no me apetece."
    hermana "Pues entonces no te dare un regalo luego"
    jugador "Esta bien, lo bajo yo"
    hide hermano 
    hide hermana
    jump finalPrologo