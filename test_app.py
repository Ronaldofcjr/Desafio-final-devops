import unittest
from app import app
import werkzeug

# Patch temporário para adicionar o atributo '__version__' em werkzeug 
if not hasattr(werkzeug, '__version__'): 
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase): 
    @classmethod 
    def setUpClass(cls): 
        # Criação do cliente de teste 
        cls.client = app.test_client()
    
    def test_login_returns_jwt(self):
        response = self.client.post("/login")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn("access_token", data)
        self.assertIsInstance(data["access_token"], str)
        self.assertGreater(len(data["access_token"]), 10)  #

    def test_protected_with_valid_token(self):
        # Primeiro gera um token através do login
        login_response = self.client.post("/login")
        token = login_response.get_json()["access_token"]

        # Depois tenta acessar a rota protegida
        protected_response = self.client.get(
            "/protected",
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(protected_response.status_code, 200)
        self.assertEqual(
            protected_response.get_json(),
            {"message": "Protected route"}
        )

    def test_get_items(self):
        response = self.client.get("/items")
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIn("items", data)
        self.assertIsInstance(data["items"], list)
        self.assertGreater(len(data["items"]), 0)  # Não pode ser vazia

if __name__ == '__main__':
    unittest.main()
