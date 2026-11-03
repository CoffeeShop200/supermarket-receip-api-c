"""Tests unitaires de départ pour les calculs de sous-total et de réduction."""

import pytest

from supermarket_receipt_api.checkout import validate_quantity


@pytest.mark.parametrize(
    "quantity",
    [
        (-5),
        (-1000),
        (-1),
        (-5),
        (-2),
    ],
)
def test_validate_quantity_invalid(quantity: int) -> None:
    with pytest.raises(ValueError):
        validate_quantity(quantity)


def validate_quantity_nominal(quantity: int, expected: int) -> None:
    """Vérifier la validation de la quantité.

    Aucun effet de bord ni application HTTP.

    Args:
        quantity (int): Quantité fournie par pytest.
        unit (str): Unité de vente du cas paramétré.
        expected (int): Quantité attendue après validation.

    Returns:
        None: Le test réussit si la quantité validée correspond à l'attendu.

    Raises:
        AssertionError: Si la quantité validée diffère de expected.
    """
    assert validate_quantity(quantity) == expected
