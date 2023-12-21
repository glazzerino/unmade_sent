import unittest
from prototype import MixtralInstructModel

class TestMixtralInstructModel(unittest.TestCase):
    def setUp(self):
        self.model = MixtralInstructModel()

    def test_correct_result(self):
        prompt = """
        You will be given a single review of a product. 

        The general information of the product is the following: 
        Extiende tu cobertura wifi eero: un extensor eero 6 agrega hasta 1500 pies cuadrados de cobertura Wi-Fi 6 a tu sistema wifi eero de malla existente.
        Requiere una red eero: los extensores eero 6 requieren una red eero existente. Puedes agregar tantos extensores eero 6 como necesites para maximizar la cobertura en toda tu casa.
        Configuración en minutos: la aplicación eero te guía para agregar un extensor eero 6 y es retrocompatible con generaciones anteriores de Wi-Fi.
        Dile adiós a la falta de señal y a esperar que los sitios carguen: eero usa la tecnología TrueMesh para enrutar el tráfico de manera inteligente y reducir las caídas del Internet, de modo que puedas reproducir en línea con confianza videos de 4K, juegos y videoconferencias.
        Mejora con el tiempo: las actualizaciones automáticas proporcionan lo último y lo mejor en wifi, y al mismo tiempo, mantienen tu red segura.

        ###END###
        
        Now consider the following review:
        We recently moved into a new home and needed wifi throughout the house. The house is super old with really thick floors and walls, and we were concerned about signal strength. We chose the Eero system for a few reasons and we've been really happy with it.
        One: It's incredibly easy to setup. You follow the instructions to plug in the Eero, then download and register the app on your phone, then you're done! The extenders are equally easy to use; you just plug them in and register them in the phone app. Need to plug something (like a printer) directly into the network because it doesn't have a wifi card? The Eero has a single ethernet output port on the back and you can plug a printer directly into that or (even better!) plug in a switch (we use the NetGear 8-Port Gigabit Ethernet Unmanaged Switch GS608) to the Eero and use that as an extension bridge to take on multiple ethernet lines. And I know all that might sound complicated but it is really SO EASY to set all this up. Plug-and-play!
        Two: It's so good at juggling network traffic. Eero maintains two networks--a 2.4 GHz and a 5 GHz--rolled up as one and manages what needs to be on the 2.4 (Echo/Alexa and most "smart" devices) and what needs to be on the 5 (everything else, like your laptops and televisions). Eero also juggles which items need to be using the main Eero device and which need to be on the extenders you may choose to scatter throughout the house. You do not have to manage ANY of that; the Eero does it all automatically and seamlessly.
        
        ###END###

        Based on this review: 
        reply easy-ui-true if the review mentions that the UI is easy to use, easy-ui-false otherwise. easy-ui-na if the review does not mention the UI.  

        output only the reply
        """
        expected_output = "easy-ui-true"
        self.model.set_prompt(prompt)
        completion = self.model.get_completion()
        content = completion.choices[0].message.content.strip()
        self.assertEqual(content, expected_output)


if __name__ == "__main__":
    unittest.main()