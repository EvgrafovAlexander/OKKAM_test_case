from web.readers import audiences_reader


async def get_percent_data(first_condition: str, second_condition: str):
    data = await audiences_reader.get_percent_data(first_condition, second_condition)
    return data