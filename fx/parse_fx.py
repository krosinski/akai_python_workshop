import datetime 

tm_parse = lambda x: datetime.datetime.strptime(x, '%d.%m.%Y %H:%M:%S.%f')

FIELD_MAP = {
    0: (tm_parse, "rate_tm"),
    1: (float, "open_price"),
    2: (float, "close_price"),
    3: (float, "high_price"),
    4: (float, "low_price"),
    5: (float, "volume")
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
    #TODO: implement

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
    ["2014-02-01", "test", "1234"]
    -> {"a": date(2014, 2, 1)
        "b": "test",
        "c": 123
        }
    """
    #TODO: replace FIELD_MAP dummy functions with appropriate type parsing
    return {FIELD_MAP[i][1]: FIELD_MAP[i][0](field)
            for i, field in enumerate(row)}

class TrendMixin:

    def should_buy(self):
        return self.close_price > self.open_price

    def should_sell(self):
        return self.close_price < self.open_price

class BaseRate:

    FIELDS = []

    def __init__(self, **kwargs):
        """Sets only fields that are specified 
        """
        #TODO: implement setting the right instance fields
        for key in self.FIELDS:
            setattr(self, key, kwargs[key])

    def should_buy(self):
        raise NotImplementedError()

    def should_sell(self):
        raise NotImplementedError()

class GeneralInfoRate(BaseRate):
    FIELDS = ['rate_tm', 'close_price']


class SpecificInfoRate(TrendMixin, BaseRate):
    #TODO: MRO, will trend predictions work?
    FIELDS = ['rate_tm', 'close_price', 'open_price', 'high_price',
              'low_price', 'volume']
    

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

        general_rates.append(GeneralInfoRate(**processed_row))
        specific_rates.append(SpecificInfoRate(**processed_row))

        assert not hasattr(general_rates[0], "volume")
        assert hasattr(specific_rates[0], "volume")

        try:
            general_rates[0].should_buy()
            assert False, "NotImplemented expected"
        except NotImplementedError:
            pass

        assert specific_rates[0].should_buy() ^\
            specific_rates[0].should_sell()


