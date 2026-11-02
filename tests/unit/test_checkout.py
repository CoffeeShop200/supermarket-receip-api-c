"""Tests unitaires de départ pour les calculs de sous-total et de réduction."""

import pytest

from supermarket_receipt_api.checkout import line_subtotal_cents, percentage_discount_cents




@pytest.mark.parametrize(
    "unit_price_cents, quantity, unit, expected",
    [(100, 2, "piece", 200), (199, 1000, "gram", 199), (199, 2000, "gram", 398)],
)
def test_line_subtotal_nominal(
    unit_price_cents: int, quantity: int, unit: str, expected: int
) -> None:
    """Vérifier des calculs de sous-total.

    Aucun effet de bord ni application HTTP.

    Args:
        unit_price_cents (int): Prix unitaire en centimes fourni par pytest.
        quantity (int): Quantité de pièces ou de grammes fournie par pytest.
        unit (str): Unité de vente du cas paramétré.
        expected (int): Montant brut attendu en centimes.

    Returns:
        None: Le test réussit si le montant calculé correspond à l'attendu.

    Raises:
        AssertionError: Si le montant calculé diffère de expected.
    """
    assert line_subtotal_cents(unit_price_cents, quantity, unit) == expected


@pytest.mark.parametrize(
    "subtotal_cents, discount_percent, expected",
    [(1000, 20, 200), (1200, 10, 120), (800, 25, 200)]
    + [(100 * amount_euros, 10, 10 * amount_euros) for amount_euros in range(20, 114)],
)
def test_percentage_discount_cents(
    subtotal_cents: int, discount_percent: int, expected: int
) -> None:
    """Vérifier des calculs de réduction en pourcentage.

    Aucun effet de bord ni application HTTP.

    Args:
        subtotal_cents (int): Montant brut en centimes.
        discount_percent (int): Pourcentage de réduction.
        expected (int): Réduction attendue en centimes.

    Returns:
        None: Le test réussit si la réduction calculée correspond à l'attendu.

    Raises:
        AssertionError: Si la réduction calculée diffère de expected.
    """
    assert percentage_discount_cents(subtotal_cents, discount_percent) == expected


def line_subtotal_cents(unit_price_cents: int, quantity: int, unit: str) -> int:
    """Calculer le brut d'une ligne avant réduction, en centimes entiers.

    Les quantités doivent être agrégées avant cet appel. Aucun effet de bord.

    Args:
        unit_price_cents (int): Prix positif ou nul en centimes par pièce ou kilogramme,
            hors booléen.
        quantity (int): Quantité strictement positive en pièces ou grammes, hors booléen.
        unit (str): Unité "piece" ou "gram". Pour "gram", le prix est par kilogramme.

    Returns:
        int: Montant brut arrondi au centime, avec le demi vers le haut.

    Raises:
        TypeError: Si un argument a un type invalide, y compris un booléen pour un entier.
        ValueError: Si le prix est négatif, la quantité n'est pas strictement positive
            ou l'unité n'est ni "piece" ni "gram".
    """
    if type(unit_price_cents) is not int:
        raise TypeError("unit_price_cents doit être un entier en centimes, hors booléen.")
    if unit_price_cents < 0:
        raise ValueError("unit_price_cents doit être supérieur ou égal à 0.")
    validate_quantity(quantity)
    if type(unit) is not str:
        raise TypeError("unit doit être une chaîne : piece ou gram.")
    if unit not in {"piece", "gram"}:
        raise ValueError("unit doit être piece ou gram ; le prix au poids est par kilogramme.")
    denominator = 1000 if unit == "gram" else 1
    return round_half_up(unit_price_cents * quantity, denominator)

