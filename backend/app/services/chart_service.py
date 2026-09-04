def decide_chart(query_result: list[dict]) -> dict:

    if not query_result:
        return {
            "chart_type": "none",
            "x": [],
            "y": []
        }

    first_row = query_result[0]

    #  Date / month column -> Line chart

    date_key = None   

    for key in first_row.keys():
        key_lower = key.lower()

        if "date" in key_lower or "month" in key_lower:
            date_key = key
            break

    if date_key:
        numeric_key = None

        for key, value in first_row.items():
            if key==date_key:
                continue

            if isinstance(value, (int, float)):
                numeric_key = key
                break

        if numeric_key:
            return {
                "chart_type":"line",
                "x":[row.get(date_key) for row in query_result],
                "y":[row.get(numeric_key) for row in query_result]
            }    


    # Multiple rows + category + numeric -> Bar

    if len(query_result) > 1:
        category_key = None
        numeric_key = None

        for key, value in first_row.items():
            if isinstance(value, (int, float)):
                if numeric_key is None:
                    numeric_key = key
            else:
                if category_key is None:
                    category_key = key

        if category_key and numeric_key:
            return {
                "chart_type": "bar",
                "x": [row.get(category_key) for row in query_result],
                "y": [row.get(numeric_key) for row in query_result],
            }


    return {
        "chart_type": "none",
        "x": [],
        "y": [],
    }    
