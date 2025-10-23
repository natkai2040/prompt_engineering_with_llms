def index_minimum(records):
    if not records:
        return None
    min_record = min(records, key=lambda record: record[1])
    return min_record[0]