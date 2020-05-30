# -*- coding: utf-8 -*-
"""
Created on Fri May 22 13:16:34 2020

@author: Pablo
"""

from experta import Rule, Fact, KnowledgeEngine, AND

class Consultorio(KnowledgeEngine):
    sintoma = ""
    medicamentos = ""
    especialista = ""        

    @Rule( AND( AND( AND( Fact(tos='True'), Fact(cansancio='True') ),Fact(dolorCabeza='True')), Fact(fiebre='True')) )
    def sintomasGripe(self):
        self.sintoma = "Gripe"
        self.medicamentos = "Jarabe, Contrex y Vacuna"
        self.especialista = "Otorrino"

        
    @Rule( AND( AND( AND( Fact(escalofrios='True'), Fact(jaqueca='True') ),Fact(secrecion='True')), Fact(fiebre='True')) )
    def sintomasRubeola(self):
        self.sintoma = "Rubeola"
        self.medicamentos = "Vacuna y Paracetamol"
        self.especialista = "Médico General"
        
    @Rule( AND( AND( AND( Fact(diarrea='True'), Fact(fiebre='True') ),Fact(ictericia='True')), Fact(escalofrios='True')) )
    def sintomasMalaria(self):
        self.sintoma = "Malaria"
        self.medicamentos = "Vacuna"
        self.especialista = "Endocrinólogo"
    
    @Rule( AND( AND( Fact(diarrea='True'), Fact(nauseas='True') ),Fact(ictericia='True')) )
    def sintomasHepatitis(self):
        self.sintoma = "Hepatitis"
        self.medicamentos = "Vacuna y Paracetamol"
        self.especialista = "Médico General"
    
    @Rule( AND( AND( AND( Fact(tos='True'), Fact(cansancio='True') ),Fact(escalofrios='True')), Fact(fiebre='True')) )
    def sintomasTuberculosis(self):
        self.sintoma = "Tuberculosis"
        self.medicamentos = "Paracetamol"
        self.especialista = "Médico General"
    
    @Rule( AND( AND( Fact(cansancio='True'), Fact(nauseas='True') ),Fact(apatia='True')) )
    def sintomasAnemia(self):
        self.sintoma = "Anemia"
        self.medicamentos = "Vitamina"
        self.especialista = "Nutriólogo"
        

#engine = Consultorio()
#engine.reset()

#engine.declare(Fact(diarrea = 'True'))
#engine.declare(Fact(fiebre = 'True'))
#engine.declare(Fact(escalofrios = 'True'))
#engine.declare(Fact(ictericia = 'False'))


#engine.run()