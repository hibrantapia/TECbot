"""
TECbot - Chatbot para el Tecnológico de Monterrey
    
La función principal va a llevar una función llamada responderPregunta(inputText) que va a tomar de argumento el string que dé el usuario de la pregunta.
Buscará con un for word in pregunta para cada tupla del diccionario de la primera capa, si encuentra algo, busca otro for word en cada diccionario que diga secondLayer si encuentra algo, se sigue así hasta la capa 5.
Si no encuentra algo en alguna capa, responde hasta donde se quedó, si no encuentra algo desde la capa 1, pasa a un agente.
En cada if debe regresar el input al usuario preguntando si quiere saber algo más de la información que tiene además de responder, y se debe buscar desde esa capa.
    
Alan Uriel Merlan Esquivel - A01656612
Héctor Hibran Tapia Fernández - A01661114
Elías Eduardo Rodríguez Hernández - A01654900 
    
"""


context = ""

dictFirstLayer = {
    ("Carreras", "carreras", "carrera", "Carrera"): ["TECbot: Las carreras que ofrece el Tecnológico de Monterrey son: Ingeniería en Ciencia de Datos y Matemáticas (IDM) e Ingeniería en Sistemas Computacionales (ITC)"],
    ("Cursos", "cursos"): ["TECbot: Los cursos que ofrece el Tecnológico de Monterrey son: Cálculo Diferencial, Cálculo Integral, Álgebra Lineal, Programación Orientada a Objetos, Ecuaciones Diferenciales, Ecuaciones Diferenciales Parciales, [...]"],
    ("Becas", "becas"): ["TECbot: Las becas que ofrece el Tecnológico de Monterrey son: Becas de Excelencia Académica, Becas de Excelencia Deportiva, Becas de Excelencia Artística, Becas de Excelencia en Ciencias, Becas de Excelencia en Tecnología, Becas de Excelencia en Emprendimiento, [...]"],
    ("Servicios", "servicios",): ["TECbot: Los servicios que ofrece el Tecnológico de Monterrey son: Biblioteca, Cafetería, Laboratorios, Salones de Clase, Salones de Estudio, Salones de Juntas, [...]"],
    ("Campus", "campus"): ["TECbot: Los campus que ofrece el Tecnológico de Monterrey son: Campus Monterrey, Campus Santa Fe, Campus Querétaro, Campus Guadalajara, Campus Puebla, Campus León, [...]"],
    ("Colegiaturas", "colegiaturas",): ["TECbot: Las colegiaturas que ofrece el Tecnológico de Monterrey son: $ 15,000.00, $ 16,000.00, $ 17,000.00, $ 18,000.00, $ 19,000.00, $ 20,000.00, [...]"],
    ("Inscripciones", "inscripciones"): ["TECbot: Las inscripciones que ofrece el Tecnológico de Monterrey son en Abril y Junio, y de Octubre a Diciembre"],
    ("Humano", "humana", "persona", "real"):["TECbot: Yo no soy una persona real, soy un asistente virtual que te puede ayudar a encontrar información sobre el Tecnológico de Monterrey. ¿En qué te puedo ayudar?"],
}

dictSecondLayerCarreras = {
  ("IDM", "Ciencia de Datos", "Matemáticas", "idm"): ["TECbot: El programa de Ingeniería en Ciencia de Datos y Matemáticas está orientado a formar profesionistas que tengan una sólida formación en estadística, matemática aplicada y algoritmos de inteligencia artificial con un enfoque especial en la modelación matemática y en la simulación computacional donde a partir de los datos y su análisis poder resolver problemas de diseño, optimización y toma de decisiones."],
  ("ITC", "Sistemas Computacionales"): ["TECbot: La carrera en Ingeniería en Sistemas Computacionales se enfoca en la creación, diseño y mantenimiento de software, hardware y redes de computadoras para la solución de problemas informáticos. Los egresados podrán desempeñarse en áreas de desarrollo de software, seguridad informática, análisis de sistemas y tecnologías de la información."],
  ("ingeniería en sistemas computacionales","sistemas computacionales", "ingeniería en sistemas", "sistemas"): ["TECbot: La carrera en Ingeniería en Sistemas Computacionales se enfoca en la creación, diseño y mantenimiento de software, hardware y redes de computadoras para la solución de problemas informáticos. Los egresados podrán desempeñarse en áreas de desarrollo de software, seguridad informática, análisis de sistemas y tecnologías de la información."],
  ("ingeniería en mecatrónica","mecatrónica"): ["TECbot: La carrera en Ingeniería en Mecatrónica se enfoca en la integración de sistemas mecánicos, eléctricos y electrónicos para la creación de sistemas automatizados y de control. Los egresados podrán desempeñarse en áreas de automatización industrial, robótica, diseño de sistemas y control de procesos."],
  ("ingeniería en energías renovables","energías renovables", "ingeniería en energías renovables", "energías","renovables"): ["TECbot: La carrera en Ingeniería en Energías Renovables se enfoca en la creación y aplicación de tecnologías para la generación de energía a partir de fuentes renovables y limpias. Los egresados podrán desempeñarse en áreas de diseño y mantenimiento de sistemas de energía renovable, eficiencia energética, y en empresas relacionadas con la energía sostenible."],
  ("ingeniería en gestión empresarial","gestión empresarial", "ingeniería en gestión empresarial", "gestión","empresarial"): ["TECbot: La carrera en Ingeniería en Gestión Empresarial se enfoca en la formación de profesionales capaces de integrar soluciones tecnológicas y de innovación para el desarrollo de negocios y organizaciones. Los egresados podrán desempeñarse en áreas de análisis y mejora de procesos empresariales, desarrollo de proyectos tecnológicos y consultoría en innovación y tecnología."],
  ("gestión de la información", "gestión", "teconlogías de la información", "tecnologías", "información"): ["TECbot: La carrera en Gestión de la Información se enfoca en la gestión y organización de información en diferentes contextos, con la finalidad de optimizar su uso y acceso. Los egresados podrán desempeñarse en áreas de gestión de datos, análisis de información, seguridad de la información y en empresas relacionadas con la tecnología de la información y comunicación."],
}

dictThirdLayerCarreras = {
    ("1er semestre", "1°", "1", "primer semestre", "primer" ,"Primer Semestre"): ["TECbot: Para primer semestre encontrarás aquí la información: https://www.tec.mx/es/estudiar-en-tec/carreras"],
    ("2do semestre", "2°", "2", "segundo semestre", "segundo" ): ["TECbot: Para segundo semestre puedes encontrar la información de las carreras en el siguiente link: https://www.tec.mx/es/estudiar-en-tec/carreras"],
    ("3er semestre", "3°", "3", "tercer semestre", "tercer" ): ["TECbot: Para tercer semestre encontrarás aquí la información: https://www.tec.mx/es/estudiar-en-tec/carreras"],
    ("4to semestre", "4°", "4", "cuarto semestre", "cuarto" ): ["TECbot: Para cuarto semestre puedes encontrar la información de las carreras en el siguiente link: https://www.tec.mx/es/estudiar-en-tec/carreras"],
    ("5to semestre", "5°", "5", "quinto semestre", "quinto" ): ["TECbot: Para quinto semestre puedes encontrar la información de las carreras en el siguiente link: https://www.tec.mx/es/estudiar-en-tec/carreras"],
}

dictSecondLayerBecas = {
    ("becas de excelencia académica","excelencia académica","becas de excelencia académica","excelencia,académica"): ["TECbot: La beca de excelencia académica está dirigida a estudiantes con un alto desempeño académico y se otorga en base al promedio del último año de estudios. Los beneficios incluyen un descuento en la colegiatura y la posibilidad de realizar intercambios académicos en universidades internacionales de prestigio."],
    ("becas de excelencia deportiva","excelencia deportiva","becas de excelencia deportiva","excelencia,deportiva"): ["TECbot: La beca de excelencia deportiva está dirigida a estudiantes que se destacan en alguna disciplina deportiva. Los beneficios incluyen un descuento en la colegiatura, la posibilidad de combinar estudios con entrenamientos y participación en eventos deportivos representando a la institución."],
    ("becas de excelencia artística","excelencia artística","becas de excelencia artística","excelencia,artística"): ["TECbot: La beca de excelencia artística está dirigida a estudiantes con talento en alguna disciplina artística. Los beneficios incluyen un descuento en la colegiatura y la posibilidad de desarrollar proyectos creativos dentro y fuera de la institución."],
    ("becas de excelencia en ciencias","excelencia en ciencias","becas de excelencia en ciencias","excelencia,ciencias"): ["TECbot: La beca de excelencia en ciencias está dirigida a estudiantes con aptitudes y habilidades en el campo de las ciencias. Los beneficios incluyen un descuento en la colegiatura y la posibilidad de participar en proyectos de investigación junto a profesores de la institución."]
}

dictThirdLayerBecas = {
    ("Embajadores", "embajadores"): ["TECbot: Los embajadores del Tecnológico de Monterrey son estudiantes y alumni que representan a la universidad en eventos y actividades académicas y culturales. ¡Conócelos y únete a la comunidad!"],
    ("PrepaTec", "Prepa Tec", "prepatec", "preparatoria"): ["TECbot: PrepaTec es la preparatoria del Tecnológico de Monterrey, donde los estudiantes pueden prepararse para ingresar a la universidad con programas de alta calidad académica y formación integral. ¡Descubre nuestras opciones de bachillerato!"],
    ("Universidad", "universidad", "tec"): ["TECbot: El Tecnológico de Monterrey es una universidad de prestigio en México y Latinoamérica, con una amplia oferta académica en áreas como ingeniería, ciencias, negocios y humanidades. ¡Descubre todo lo que podemos ofrecerte!"],
}

dictSecondLayerServicios = {
    ("Admisiones", "admisión", "admisiones"): ["TECbot: Si estás interesado en estudiar en el Tecnológico de Monterrey, puedes revisar los requisitos de admisión en nuestra página web y completar tu solicitud en línea. También ofrecemos sesiones de orientación para ayudarte en el proceso."],
    ("Quejas", "queja", "reclamo"): ["TECbot: Si tienes alguna queja o reclamo, puedes comunicarte con nuestro equipo de atención al cliente a través de nuestra línea telefónica o correo electrónico. Nos esforzamos por ofrecer un excelente servicio a nuestros estudiantes y usuarios."],
    ("Idiomas", "idiomas", "lenguas"): ["TECbot: En el Tecnológico de Monterrey ofrecemos una amplia variedad de cursos de idiomas para ayudarte a desarrollar tus habilidades lingüísticas y culturales. Además, también contamos con programas de intercambio y estudio en el extranjero para que puedas practicar tus habilidades en contextos reales."],
    ("Becas", "becas", "apoyo económico"): ["TECbot: En el Tecnológico de Monterrey contamos con diversas opciones de becas y apoyo económico para ayudarte a financiar tus estudios. Estos incluyen becas académicas, deportivas, culturales, y de necesidad económica. ¡Revisa las opciones disponibles y solicita la tuya!"]
}

dictSecondLayerCampus = {
    ("campus monterrey","monterrey"): ["TECbot: El campus Monterrey se encuentra ubicado en la ciudad de Monterrey, Nuevo León. Cuenta con 4 edificios, 2 salones de clase, 2 laboratorios, 1 biblioteca, 1 cafetería, 1 salón de juntas, 1 salón de estudio, 1 salón de conferencias y 1 auditorio."],
    ("campus santa fe","santa fe"): ["TECbot: El campus Santa Fe se encuentra ubicado en la ciudad de Monterrey, Nuevo León. Cuenta con 2 edificios, 1 salón de clase, 1 laboratorio, 1 biblioteca, 1 cafetería, 1 salón de juntas, 1 salón de estudio, 1 salón de conferencias y 1 auditorio."],
    ("campus querétaro","querétaro"): ["TECbot: El campus Querétaro se encuentra ubicado en la ciudad de Querétaro, Querétaro. Cuenta con 2 edificios, 1 salón de clase, 1 laboratorio, 1 biblioteca, 1 cafetería, 1 salón de juntas, 1 salón de estudio, 1 salón de conferencias y 1 auditorio."],
    ("campus puebla","puebla"): ["TECbot: El campus Puebla se encuentra ubicado en la ciudad de Puebla, Puebla. Cuenta con 2 edificios, 1 salón de clase, 1 laboratorio, 1 biblioteca, 1 cafetería, 1 salón de juntas, 1 salón de estudio, 1 salón de conferencias y 1 auditorio."],
    ("campus guadalajara","guadalajara"): ["TECbot: El campus Guadalajara se encuentra ubicado en la ciudad de Guadalajara, Jalisco. Cuenta con 2 edificios, 1 salón de clase, 1 laboratorio, 1 biblioteca, 1 cafetería, 1 salón de juntas, 1 salón de estudio, 1 salón de conferencias y 1 auditorio."],
    ("campus méxico","méxico"): ["TECbot: El campus México se encuentra ubicado en la ciudad de México, Distrito Federal. Cuenta con 2 edificios, 1 salón de clase, 1 laboratorio, 1 biblioteca, 1 cafetería, 1 salón de juntas, 1 salón de estudio, 1 salón de conferencias y 1 auditorio."],
}

dictSecondLayerColegiaturas = {
    ("PrepaTEC", "preparatoria", "prepa"): ["TECbot: PrepaTEC es la preparatoria del Tecnológico de Monterrey. Ofrecemos una educación de alta calidad y una amplia variedad de actividades extracurriculares para ayudar a nuestros estudiantes a desarrollar sus habilidades y talentos. ¡Únete a nuestra comunidad y comienza a construir tu futuro!"],
    ("Universidad", "universidad", "carrera"): ["TECbot: El Tecnológico de Monterrey es una universidad líder en Latinoamérica, reconocida por su excelencia académica y su compromiso con la innovación y el desarrollo tecnológico. Ofrecemos una amplia variedad de carreras y programas de estudio para ayudarte a alcanzar tus metas y desarrollar tus habilidades. ¡Explora nuestras opciones y descubre lo que podemos hacer por ti!"],
    ("Unitec", "universidad", "carrera"): ["TECbot: Unitec es una de las universidades líderes en México, con una amplia variedad de carreras y programas de estudio en áreas como negocios, ingeniería, tecnología, diseño y ciencias de la salud. Ofrecemos una educación de alta calidad y un ambiente de aprendizaje innovador para ayudarte a desarrollar tus habilidades y alcanzar tus metas. ¡Únete a nuestra comunidad y comienza a construir tu futuro!"]
}


dictSecondLayerInscripciones = {
    ("Información General", "información", "general"): ["TECbot: Si estás interesado en estudiar en el Tecnológico de Monterrey, podemos brindarte información detallada sobre nuestras carreras, programas de estudio, becas, servicios, entre otros. Por favor, proporciona más detalles sobre lo que necesitas para que podamos ayudarte mejor."],
    ("Visita al Campus", "visita", "campus"): ["TECbot: Si deseas visitar uno de nuestros campus, puedes programar una visita guiada con nosotros. Durante la visita, podrás conocer nuestras instalaciones, servicios, y tendrás la oportunidad de hablar con estudiantes y profesores. ¡Te invitamos a que descubras todo lo que el Tecnológico de Monterrey tiene para ofrecer!"],
    ("Examen de Admisión", "examen", "admisión"): ["TECbot: Para estudiar en el Tecnológico de Monterrey es necesario presentar un examen de admisión. Este examen evalúa habilidades y conocimientos en diferentes áreas, y es parte importante del proceso de selección. Si deseas obtener más información sobre el examen de admisión, por favor proporciónanos tus detalles y te brindaremos toda la información que necesitas."]
}

dictFourthLayerMaterias = {
    ("Matemáticas", "matematicas", "mate"):["TECbot: La materia de introducción a las matemáticas es una materia que se imparte en el primer semestre de la carrera de Matemáticas. En esta materia se estudian los conceptos básicos de álgebra, geometría y trigonometría."],
}

dictFifthLayerProfesores = {
    ("profesor", "profesores"): ["TECbot: En el siguiente link puedes encontrar la información de los profesores: https://www.tec.mx/es/estudiar-en-tec/profesores"],
}

def responderPregunta(inputText):
    global context
    inputText= inputText + " " + context
    for key in dictFirstLayer:
        for word in key:
            if word in inputText:
                for key2 in dictSecondLayerCarreras:
                    for word2 in key2:
                        if word2 in inputText:
                            for key3 in dictThirdLayerCarreras:
                                for word3 in key3:
                                    if word3 in inputText:
                                        for key4 in dictFourthLayerMaterias:
                                            for word4 in key4:
                                                if word4 in inputText:
                                                    for key5 in dictFifthLayerProfesores:
                                                        for word5 in key5:
                                                            if word5 in inputText:
                                                                print(str(dictFifthLayerProfesores[key5]).replace('[','').replace(']','').replace("'",""), end="")
                                                                return
                                                    print(str(dictFourthLayerMaterias[key4]).replace('[','').replace(']','').replace("'",""), end="")
                                                    return
                                        for key4 in dictThirdLayerBecas:
                                            for word4 in key4:
                                                if word4 in inputText:
                                                    print(str(dictThirdLayerBecas[key4]).replace('[','').replace(']','').replace("'",""), end="")
                                                    return
                                        print(str(dictThirdLayerCarreras[key3]).replace('[','').replace(']','').replace("'",""), end="")
                                        return
                            for key3 in dictSecondLayerServicios:
                                for word3 in key3:
                                    if word3 in inputText:
                                        print(str(dictSecondLayerServicios[key3]).replace('[','').replace(']','').replace("'",""), end="")
                                        return
                            for key3 in dictSecondLayerColegiaturas:
                                for word3 in key3:
                                    if word3 in inputText:
                                        print(str(dictSecondLayerColegiaturas[key3]).replace('[','').replace(']','').replace("'",""), end="")
                                        return
                            for key3 in dictSecondLayerInscripciones:
                                for word3 in key3:
                                    if word3 in inputText:
                                        print(str(dictSecondLayerInscripciones[key3]).replace('[','').replace(']','').replace("'",""), end="")
                                        return
                            print(str(dictSecondLayerCarreras[key2]).replace('[','').replace(']','').replace("'",""), end="")
                            return
                for key2 in dictSecondLayerBecas:
                    for word2 in key2:
                        if word2 in inputText:
                            print(str(dictSecondLayerBecas[key2]).replace('[','').replace(']','').replace("'",""), end="")
                            return
                for key2 in dictSecondLayerCampus:
                    for word2 in key2:
                        if word2 in inputText:
                            print(str(dictSecondLayerCampus[key2]).replace('[','').replace(']','').replace("'",""), end="")
                            return
                print(str(dictFirstLayer[key]).replace('[','').replace(']','').replace("'",""), end="")
                return
    print("\nTECbot: No encontré la información que buscabas... Estoy comunicándote con un agente... Espera un momento por favor...\n", end="")



def main():    
   
    global context

    print("TECbot: ¡Hola, soy TECbot! ¿Cuál es tu nombre?")
    nombre = input("\nTú: ")
    print(f"\nTECbot: ¡Hola {nombre}, gusto en conocerte! Escribe alguna de las siguientes opciones.")
    print("\n - Carreras \n - Cursos \n - Becas \n - Servicios \n - Campus \n - Colegiaturas \n - Inscripciones \n  \n- Contactar Agente \n- Salir")

    while True:
        print(" ")
        inputText = input(f"{nombre}: ")
        if inputText == 'Salir' or inputText == 'salir':
            print(f"\nTECbot: ¡Gracias por chatear conmigo {nombre}, nos vemos pronto!\n")
            break
        elif inputText == "Contactar Agente" or inputText == "contactar agente":
          print(f"\nTECbot: Estoy comunicándote con un agente... Espera un momento por favor...\n")
          break
        else:
            print(f"\nTECbot: Aségurate de escribir palabras clave capa por capa mientras vayas avanzando. (Por ejemplo: Carrera - Ciencia de Datos - Primer Semestre)\n")
            responderPregunta(inputText)
            
            
if __name__ == '__main__':
    main()