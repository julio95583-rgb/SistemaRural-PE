import pytest

from src.modelos.gestor_sistema import GestorSistema


@pytest.fixture(autouse=True)
def gestor_limpio():
    GestorSistema.reiniciar()
    yield
    GestorSistema.reiniciar()
