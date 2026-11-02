"""Tests unitaires de départ pour les calculs de sous-total et de réduction."""

import pytest

from supermarket_receipt_api.checkout import line_subtotal_cents, three_for_two_discount_cents,round_half_up, validate_quantity




@pytest.mark.parametrize(
    "quantity, expected",
    [
        (2, 2),
        (1000, 10001),
        (2000, 2000),
        (5, 5),
        (7, 7),
    ],
)
def test_validate_quantity_nominal(
    quantity: int,expected: int
) -> None:
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


