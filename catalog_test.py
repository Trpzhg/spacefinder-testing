def filter_by_metro(objects, metro):
    """Возвращает объекты, расположенные у выбранной станции метро."""
    return [item for item in objects if item.get("metro") == metro]


def test_filter_by_metro():
    objects = [
        {"name": "Nevsky Hub", "metro": "Невский проспект"},
        {"name": "Loft Work", "metro": "Петроградская"},
    ]
    result = filter_by_metro(objects, "Петроградская")
    assert result == [{"name": "Loft Work", "metro": "Петроградская"}]
