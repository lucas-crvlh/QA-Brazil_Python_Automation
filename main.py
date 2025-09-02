import data
import helpers

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado a servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução")

    def test_set_route(self):
        print("função criada para definir a rota")
        # Adicionar em S8
        pass

    def test_select_plan(self):
        print("função criada para definir a rota")
        # Adicionar em S8
        pass

    def test_fill_phone_number(self):
        print("função criada para definir a rota")
        # Adicionar em S8
        pass

    def test_fill_card(self):
        print("função criada para definir a rota")
        # Adicionar em S8
        pass

    def test_comment_for_driver(self):
        print("função criada para definir a rota")
        # Adicionar em S8
        pass

    def test_order_blanket_and_handkerchiefs(self):
        print("função criada para definir a rota")
        # Adicionar em S8
        pass

    def test_order_2_ice_creams(self):
        number_of_ice_creams = 2
        for count in range(number_of_ice_creams):
            print("função criada para definir a rota")
            # Adicionar em S8
            pass

    def test_car_search_model_appears(self):
        print("função criada para definir a rota")
        # Adicionar em S8
        pass
