from app.schemas.routing import RoutingResult


result = RoutingResult(
    route="SQL",
    reasoning="The question requires database information",
    confidence=0.95
)

print(result)
