import datetime

FIELD_MAP = {
    0: (str, "rate_tm"),
    1: (str, "open_price"),
    2: (str, "close_price"),
    3: (str, "high_price"),
    4: (str, "low_price"),
    5: (str, "volume")
}

def load_raw_data(data_file):
    """Loads data from a CSV file
    each row should be represented as a list of unicode fields 
    should skip first row -> labels
    example:
    [
        [u"a", u"123", u"123.56",],
        [u"b", u"123", u"123.77",], 
        #....   et 
    ]
    """
    output_data = []
    skipped_title = False
    with open(data_file, 'rt') as f:
        for line in f:
            if not skipped_title:
                skipped_title = True
                continue
            output_data.append(line.split(','))
    return output_data

def parse_row(row):
    """Maps a list of fields into a dictionary with preprocessed data
    example:
    ["2014-02-01", "123.12",]
    -> {"rate_tm": date(2014, 2, 1),
        "open_price": 123.12,
        }
    """
    #TODO: replace FIELD_MAP dummy functions with appropriate type parsing
    #return a dictionary of {field_name: parsed_value}
    #Hint: use enumerate(row) and dictionary comprehansion
    return {}

if __name__ == "__main__":
    general_rates = []
    specific_rates = []
    data = load_raw_data("eurusd.csv")
    assert len(data) == 1000
    for row in data:
        assert len(row) == 6

    for processed_row in (parse_row(r) for r in data):
        assert isinstance(processed_row, dict)
        assert isinstance(processed_row['rate_tm'], datetime.datetime)
        assert isinstance(processed_row['open_price'], float)
        assert isinstance(processed_row['close_price'], float)
