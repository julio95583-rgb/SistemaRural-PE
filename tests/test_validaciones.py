import pytest
from src.utils.validaciones import validar_dni

def test_existencia_validar_dni():
    assert callable(validar_dni)
