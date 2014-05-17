
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

    return output_data

    

if __name__ == "__main__":
    data = load_raw_data("eurusd.csv")
    assert len(data) == 1000
    for row in data:
        assert len(row) == 6
