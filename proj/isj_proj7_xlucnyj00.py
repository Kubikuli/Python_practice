#!/usr/bin/env python3

class TimeSeriesDB(dict):
    """
    Database based on standard Python dict
    Allows to save keys with list of pairs consisting of timestamp and value
    and allows to search by key or key and timestamp
    """

    def __setitem__(self, key, pair):
        """
        Stores new pair to given key
        Ensures timestamps are inserted in increasing order for each key
        """
        if isinstance(key, str) and isinstance(pair, tuple) and len(pair) == 2:
            timestamp, val = pair

            if key not in self:
                # Key doesn't exist yet
                super().__setitem__(key, [])

            data = super().__getitem__(key)

            # Check if given timestamp is >= than last inserted one
            if data and timestamp <= data[-1][0]:
                raise ValueError("Timestamps must be increasing in value.")
            data.append((timestamp, val))
        else:
            raise ValueError("Invalid inserting format")

    def __getitem__(self, key):
        """
        Returns value associated to given key and timestamp
        or first value with stored_timestamp <= timestamp
        or value of last pair inserted if only key is given
        """
        # Search by key
        if isinstance(key, str):
            data = super().__getitem__(key)
            if not data:
                raise KeyError("No values for given key")
            return data[-1][1]

        # Search by key and timestamp
        elif isinstance(key, tuple) and len(key) == 2:
            key, timestmp = key
            data = super().__getitem__(key)
            if not data:
                raise KeyError("No values for given key")

            # Traverse the data backwards until finding first element with equal or smaller timestamp
            reversed_data = data[::-1]
            for ts, val in reversed_data:
                if ts <= timestmp:
                    return val
            raise KeyError("No timestamp stored with lower or equal value than given")

        else:
            raise KeyError("Invalid search format.")


def test():
    time_db = TimeSeriesDB()
    time_db['vibr'] = (1, 'low')
    time_db['vibr'] = (5, 'mid')
    time_db['vibr'] = (8, 'low')
    time_db['vibr'] = (12, 'high')
    time_db['temp'] = (2, 37.6)
    time_db['temp'] = (4, 37.2)
    time_db['temp'] = (17, 37.7)


    assert time_db[('vibr', 1)] == 'low'
    assert time_db[('vibr', 4)] == 'low'
    assert time_db[('vibr', 7)] == 'mid'
    assert time_db['temp'] == 37.7


if __name__ == '__main__':
    test()
