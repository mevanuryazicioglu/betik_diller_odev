def clean_data(rows: list[dict]) -> list[dict]:
    cleaned = []
    for r in rows:
        name = r["name"].strip() if r["name"] else ""
        city = r["city"].strip() if r["city"] else ""
        age = r["age"].strip() if r["age"] else ""

        if not age.isdigit():
            continue

        cleaned.append({
            "name": name,
            "age": int(age),
            "city": city
        })
    return cleaned


def stats(rows: list[dict]) -> dict:
    if not rows:
        return {"count": 0, "avg_age": 0, "by_city": {}}

    ages = [r["age"] for r in rows]
    by_city = {}
    for r in rows:
        by_city[r["city"]] = by_city.get(r["city"], 0) + 1

    return {
        "count": len(rows),
        "avg_age": sum(ages) / len(ages),
        "by_city": by_city
    }


def build_report(st: dict) -> str:
    lines = [
        "Rapor",
        "",
        f"Geçerli kayıt sayısı: {st['count']}",
        f"Ortalama yaş: {st['avg_age']:.2f}",
        "Şehir dağılımı:"
    ]
    for c, n in st["by_city"].items():
        lines.append(f"{c}: {n}")
    return "\n".join(lines) + "\n"
