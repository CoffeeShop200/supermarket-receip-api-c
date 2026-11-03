from fastapi.testclient import TestClient

from supermarket_receipt_api.main import app

client = TestClient(app)


def test_health_endpoint() -> None:
    """Vérifier que l'endpoint /health répond correctement.

    Aucun effet de bord ni application HTTP.

    Returns:
        None: Le test réussit si le code de statut est 200 et le corps JSON est {"status": "ok"}.

    Raises:
        AssertionError: Si le code de statut ou le corps JSON diffère de l'attendu.
    """
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_basket_endpoint() -> None:
    """Vérifier que l'endpoint /checkout répond correctement avec un panier valide.

    Aucun effet de bord ni application HTTP.

    Returns:
        None: Le test réussit si le code de statut est 200 et le corps JSON contient les clés attendues.

    Raises:
        AssertionError: Si le code de statut ou le corps JSON diffère de l'attendu.
    """
    response = client.post(
        "/checkout",
        json={"items": [{"product_id": "apples", "quantity": 3}]},
    )

    assert response.status_code == 200
    assert "total_cents" in response.json()
    assert "lines" in response.json()


def test_basket_endpoint_red_run() -> None:
    """Vérifier que l'endpoint /checkout répond correctement avec un panier valide.

    Aucun effet de bord ni application HTTP.

    Returns:
        None: Le test réussit si le code de statut est 200 et le corps JSON contient les clés attendues.

    Raises:
        AssertionError: Si le code de statut ou le corps JSON diffère de l'attendu.
    """
    response = client.post(
        "/checkout",
        json={"items": [{"product_id": "apples", "quantity": 3}]},
    )

    assert response.status_code == 200
    assert "total_cents" in response.json()
    assert "lines" in response.json()
