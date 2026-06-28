# Pruebas para el módulo principal de la aplicación Wolfram Alpha

import unittest
from src.utils.helpers import format_query, validate_response


class TestHelpers(unittest.TestCase):
    def test_format_query(self):
        """Prueba que la función format_query formatea correctamente la consulta."""
        query = "What is the speed of light?"
        expected = "What+is+the+speed+of+light?"
        self.assertEqual(format_query(query), expected)

    def test_validate_response(self):
        """Prueba que la función validate_response valida correctamente la respuesta."""
        valid_response = {"queryresult": {"pods": []}}
        invalid_response = {}
        
        self.assertTrue(validate_response(valid_response))
        self.assertFalse(validate_response(invalid_response))


if __name__ == "__main__":
    unittest.main()
